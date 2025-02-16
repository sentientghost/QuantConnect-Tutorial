![qcBanner](images/QuantConnectAndLeanEngineLogo.png)

# QUANTCONNECT TUTORIAL
Starter project to understand QuantConnect and Lean Engine, following alongside the [QuantConnect YouTube Playlist][qcYouTubePlaylist]

# Table of Contents
- [Project Description](#project-description)
- [Repository Structure](#repository-structure)
- [Quickstart](#quickstart)
    - [Pre-requistites](#pre-requisites)
    - [Setup](#setup)
- [Trading Strategies](#trading-strategies)
    - [Buy the Close, Sell the Open](#buy-the-close-sell-the-open)
    - [Power Earnings Gap](#power-earnings-gap)
    - [Backtesting Strategies](#backtesting-strategies)
- [Useful Knowledge](#useful-knowledge)
    - [Definitions](#definitions)
    - [Commands](#commands)
- [Version Tracker](#version-tracker)
- [Resources](#resources)

# Project Description
## QuantConnect
QuantConnect is an algorithmic trading browser-based platform that lets you develop, test and execute strategies

## Lean Engine
LEAN is an open-source quantitative trading technology. Research, backtest, optimize, and then live-trade on hundreds of venues

# Repository Structure
```
Landing Page: Explains repository structure
├── quantconnect-lean-tutorial: QuantConnect YouTube Playlist
│   ├── data: Sample datasets for different assets
|   ├── trade-spy: Project for 1st video (static universes)
|   ├── power-earnings-gap-scanner: Project for 2nd video (dynamic universes)
│   └── lean.json: Configurations for lean engine
|
├── requirements.txt
├── .gitignore
└── README.md
```

# Quickstart
## Pre-requisites 
1. Install [Python][pythonDownloadLink]
2. Install [Docker Desktop][dockerDesktopDownloadLink]
3. Create [QuantConnect][qcAccount] account and request token information (`User ID` and `Token API`)

## Setup
1. Create virtual environment
```
python -m venv venv
```
2. Install lean engine
```
pip install lean
```
3. Configure autocomplete for QuantConnect
```
pip install --upgrade quantconnect-stubs
```
4. Initialize lean
```
lean init
```
5. Create project
```
lean create-project trade-spy
```

# Trading Strategies
## Buy the Close, Sell the Open
A simple strategy for trading SPY, the ETF that tracks the S&P 500. Several articles noted that majority of stock gains occur overnight, whereby holding SPY structly overnigh yields 4% higher CAGR and experienes 44% less volatility.

## Power Earnings Gap
A stock that gaps up after reporting strong earnings and closes the day by printing a strong candle. Typically it means that the company's earnings were much better than expected, which can trigger a strong multi-month move.

## Backtesting Strategies
1. Ensure docker is installed and running
2. Run backtest command locally
```
lean backtest <name_of_project>
```
3. Run backtest command on the cloud
```
lean cloud push
lean cloud backtest <name_of_project>
```
4. Run backtest command on the cloud with graph
```
lean cloud backtest <name_of_project> --push --open
```

# Useful Knowledge
## Definitions
- **Static and Dynamic Universes:** Filtering thousands of stocks down based on specifications that meet the strategy's criteria to create a universe of tradable assets

## Commands
- Run `lean create-project "My Project"` to create a new project with starter code
- Run `lean cloud pull` to download all your QuantConnect projects to your local drive
- Run `lean backtest "My Project"` to backtest a project locally with the data in data/

# Version Tracker
| Package           | Version           |
| :---              | :---:             |
| Python            | 3.12.3            |
| Pip               | 24.0.0            |
| Lean              | 1.0.214           |

# Resources
- [QuantConnect YouTube Playlist][qcYouTubePlaylist]
- [QuantConnect – A Complete Guide][qcCompleteGuide]
- [QuantConnect - AutoComplete Documentation][qcAutoCompleteDocLink]
- [SpintWig - Comparative Investment Strategies][spintWig]
- [LEAN Documentation][leanDocLink]
- [Trillion Dollar Equation][trillionYTLink]

[comment]: # (Variables)
[pythonDownloadLink]: https://www.python.org/doc/versions/
[dockerDesktopDownloadLink]: https://www.docker.com/products/docker-desktop/
[qcAccount]: https://www.quantconnect.com/
[qcYouTubePlaylist]: https://www.youtube.com/playlist?list=PLvzuUVysUFOt_xUZnbXxvqi5eyWHSgiWA
[qcCompleteGuide]: https://algotrading101.com/learn/quantconnect-guide/
[qcAutoCompleteDocLink]: https://www.quantconnect.com/docs/v2/lean-cli/projects/autocomplete
[spintWig]: https://spintwig.com/
[leanDocLink]: https://www.lean.io/docs/v2/
[trillionYTLink]: https://www.youtube.com/watch?v=A5w-dEgIU1M