# region imports
from AlgorithmImports import *
# endregion

class ScheduleBuyOnCloseSellOnOpen(QCAlgorithm):

    def initialize(self):
        # Locally Lean installs free sample data, to download more data please visit https://www.quantconnect.com/docs/v2/lean-cli/datasets/downloading-data
        self.set_start_date(2002, 8, 5)  # Set Start Date
        self.set_end_date(2022, 8, 5)  # Set End Date
        self.set_cash(1000000)  # Set Strategy Cash
        self.security = self.add_equity("SPY", Resolution.MINUTE)
        self.security.set_fee_model(ConstantFeeModel(0))
        # self.set_brokerage_model(BrokerageName.INTERACTIVE_BROKERS_BROKERAGE, AccountType.MARGIN) 
        self.set_benchmark("SPY")
        self.schedule.on(self.date_rules.every_day(self.security.symbol), self.time_rules.after_market_open(self.security.symbol, 1), self.sell_open)
        self.closing_order_sent = False

    def sell_open(self):
        if self.portfolio.invested:
            self.liquidate()
            self.closing_order_sent = False

    def on_data(self, data: Slice):
        """on_data event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """
        if self.Time.hour == 15 and not self.closing_order_sent and not self.portfolio.invested:
            quantity = self.calculate_order_quantity(self.security.symbol, 1)
            self.market_on_close_order(self.security.symbol, quantity)
            self.closing_order_sent = True

    def on_order_event(self, order_event):
        return super().on_order_event(order_event)