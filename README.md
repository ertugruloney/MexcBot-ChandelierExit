# Trading Bot
This is a Python script that implements a trading bot using the ccxt library. The bot fetches candlestick data from the MEXC exchange, performs technical analysis on the data, and executes trading operations based on predefined signals.

# Prerequisites

Before running the trading bot script, make sure you have the following:

- Python 3.x installed
- Required Python packages installed (ccxt, pandas, numpy, matplotlib, plotly, yfinance, finta)
# Installation
1. Clone the repository or download the script file.

```bash
git clone https://github.com/your_username/trading-bot.git

```

2. Install the required Python packages.

```bash
pip install ccxt pandas numpy matplotlib plotly yfinance finta

```
3. Configure API Key and Secret

    - Obtain API credentials from the MEXC exchange.
    - Open the script file and replace the empty strings in the exchange initialization with your API key and secret.
``` python
exchange = ccxt.mexc({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET'
})

```
# Usage
1. Run the script.

``` bash
python trading_bot.py

```


2. The bot will start fetching candlestick data from the MEXC exchange for the specified symbol and timeframe.
3. Technical analysis indicators (ATR and chandelier exits) will be calculated based on the fetched data.
4. Trading signals will be generated based on the calculated indicators.
5. The bot will check the account balance and execute buy or sell orders according to the signals.
6. The process will continue indefinitely until the script is interrupted.

# Customization

You can customize the behavior of the trading bot by modifying the following parameters:

- `symbol`: The trading pair symbol to be traded (e.g., KAS/USDT).
- `timeframe`: The timeframe for the candlestick data (e.g., 15m).
- `atr_period`: The period used for calculating the Average True Range indicator.
- `start_investment`: The initial investment amount for trading.
- `df.tail(400)`: The number of recent data points to consider for analysis and trading. Adjust this value based on your requirements.

You can also modify the trading logic by updating the calculate_signals function according to your specific trading strategy.

# Disclaimer
- This trading bot is provided for educational and informational purposes only. Use it at your own risk.
- Always exercise caution and perform thorough testing before using any automated trading system with real funds.
- The trading strategy implemented in this script is a simple example and may not be suitable for all market conditions or financial instruments.
