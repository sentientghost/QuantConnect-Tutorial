# region imports
from datetime import timedelta
from AlgorithmImports import *
# endregion

class PowerEarningsGap(QCAlgorithm):

    def initialize(self):
        # Locally Lean installs free sample data, to download more data please visit https://www.quantconnect.com/docs/v2/lean-cli/datasets/downloading-data
        self.set_start_date(2021, 6, 3)  # Set Start Date
        self.set_end_date(2021, 8, 3)  # Set End Date
        self.set_cash(100000)  # Set Strategy Cash
        self.add_universe(self.coarse_filter, self.fine_filter)

        self.SPY = self.add_equity("SPY").symbol
        self.schedule.on(self.date_rules.every_day("SPY"), self.time_rules.after_market_open("SPY", 1), self.after_market_open)

    def coarse_filter(self, universe: List[CoarseFundamental]):
        # Filter universe
        universe = [asset for asset in universe if asset.dollar_volume > 1000000 and asset.price > 10 and asset.has_fundamental_data]

        # Sort universe in descending
        sorted_by_dollar_volume = sorted(universe, key=lambda asset: asset.dollar_volume, reverse=True)

        # Select first 500
        top_sorted_dollar_volume = sorted_by_dollar_volume[:500]

        # Return list of symbol objects
        symbol_objects = [asset.symbol for asset in top_sorted_dollar_volume]

        # Used for debugging
        # ticker_symbol_values_only = [symbol.value for symbol in symbol_objects]
        # self.debug(ticker_symbol_values_only)

        return symbol_objects

    def fine_filter(self, coarse_universe: List[FineFundamental]):
        yesterday = self.time - timedelta(days=1)  
        
        fine_universe = [asset.symbol for asset in coarse_universe if asset.earning_reports.file_date.value == yesterday and asset.market_cap > 1e9]
        
        # ticker_symbol_values_only = [symbol.value for symbol in fine_universe]
        # self.debug(ticker_symbol_values_only)

        return fine_universe
    
    def after_market_open(self):
        for security in self.active_securities.values:
            symbol = security.symbol

            if symbol == self.SPY:
                continue

            history_data = self.history(symbol, 7, Resolution.DAILY)

            try: 
                open_day_after_earnings = history_data['open'][-1] 
                close_day_after_earnings = history_data['close'][-1] 
                high_day_after_earnings = history_data['high'][-1] 
                close_day_before_earnings = history_data['close'][-2] 

            except:
                self.debug(f"History data unavailable for {symbol.value}")
                continue 

            price_gap = open_day_after_earnings - close_day_before_earnings
            percent_gap = price_gap / close_day_before_earnings
            close_strength = (close_day_after_earnings - open_day_after_earnings) / (high_day_after_earnings - open_day_after_earnings)

            if percent_gap > 0.05:
                self.debug(f"{symbol.value} gapped up by {percent_gap} - {close_day_before_earnings} {open_day_after_earnings}")

                if close_day_after_earnings > close_day_before_earnings and close_strength > 0.5:
                    self.debug(f"{symbol.value} closed strong")
                    self.market_order(symbol, 100)
                    self.limit_order(symbol, -100, close_day_after_earnings* 1.02)
                else:
                    self.debug(f"{symbol.value} faded after earnings")

