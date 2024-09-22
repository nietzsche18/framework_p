# Equities framework

## Description
**This project aims at backtesting intraday strategies on US equities using ML.**

It considers many variables such as float, premarket activity, gap at the open etc.

The goal is to make it easy to test different ML algorithms and different filters / market conditions. 
=> it aims at identifying patterns on whether a gaping stock might be active during session, whether it would make a strong continuation move or rather a slow bleeding move.

## Workflow 

This repo provides a Strategy Class that lets the user test a new strategy by only calling a new instance of this class. Those instances are available in *StrategyInstances.py* 

What happens underneath: 
1. Data collection : retrieves ohlc and fundamental data
2. Data calculation :  calculates over 100 indicators (full list below)
3. Preparation (PrepClass): prepares dataframe, this is where all the filters selected in the Strategy Instance are applied

    - global filters : filters applied to narrow the selection. Example: market cap < 10b; average volume > 10mUSD ...

    - strategy filter : what will need to be predicted by the ML algorithm. Example: stocks that move more than 1% one hour after the open but don't go below -1%. 

    - column filter : we can choose which data will be given to train the algorithm and make the predictions (100 indicators might be too much) 

4. Train / test (Strategy Class): trains and tests based on the selected algorithms of the Strategy Instance (TODO: add more algos)

5. Calculates result KPI based on test predictions : compounded_return, cagr, average_trade, win_rate, max_drawdown, max_consecutives_losses, sharpe_ratio, sortino_ratio




## Architecture
### data_collection 
*This folder aims at preparing data for backtesting by: retrieving, storing data and calculating indicators*

- fin_functions.py : functions that retrieve ohlc, float, days until earnings and other fundamental data related to results

     -> requires API keys for Polygon & for financial modeling prep

     -> many other data could be added based on financialmodelingprep API (TODO)

- analysis.py : functions that calculates intraday metrics 

- main.py : call fin_functions and analysis.py to retrieve data, and then calculates additional metrics (all variables are detailed below)

### backtest
*This folder provides algorithms that backtest strategies*

- PrepClass : filters the dataframe to selected variables ; prepares dataframe for training / prediction (calculate y)  

- Strategy Class : this is where the algorithms are. it runs the algorithms based on what was prepared in PrepClass. 

- Strategy Instances: this is where the strategy are "built", user can select which algorithms he wants to run, using which variables and under which conditions. Testing a new strategy is as simple as that. 

- results.py : calculates compounded_return, cagr, average_trade, win_rate, max_drawdown, max_consecutives_losses, sharpe_ratio, sortino_ratio
  
- display_graphs.py : shows the graphs of each trades on the daily chart 

- metrics.py contains additional metrics that could be added to calculate performance of the strategy


### notebooks
*Jupyter notebooks for data analysis and ML testing*


## Variables

- ticker: The stock symbol or trading code.
- date: The date of the trading session.
- week_day: The day of the week.
- freeFloat: The number of shares available for trading.
- floatShares: The total number of shares available for public trading.
- market_cap: The total market value of the company's outstanding shares.
- outstandingShares: The total number of shares currently held by all shareholders.
- volume: The total number of shares traded during the session.
- dollar_volume: The total dollar value of shares traded during the session.
- average_volume: The average number of shares traded over 20 daily candles.
- average_volume_previous_day: The average volume of shares traded on the previous day.
- average_dollar_volume_previous_day: The average dollar volume of shares traded on the previous day.
- relative_volume: The ratio of current volume to average volume.
- float_rotation: The number of times the float has been traded on the day.
- pm_float_rotation: The float rotation during pre-market trading.
- pm_volume: The volume of shares traded during pre-market trading.
- average_dollar_volume_per_transaction: The average dollar value per transaction.
- gap: The difference between the previous day's close and the current day's open.
- x_day_high_at_open: The highest price over a specified number of days at the open.
- x_day_low_at_open: The lowest price over a specified number of days at the open.
- previous_day_close: The closing price of the previous trading session.
- sigma: The standard deviation of the stock's price.
- sigma_at_open: The standard deviation at the opening price.
- sigma_previous_day: The standard deviation of the previous day's price.
- sigma_change_at_open: The change in standard deviation at the open.
- sigma_percent_at_open: The percentage change in standard deviation at the open.
- max_up: The maximum upward movement during the session.
- max_down: The maximum downward movement during the session.
- open_from_20sma: The opening price relative to the 20-day simple moving average.
- open_from_50sma: The opening price relative to the 50-day simple moving average.
- open_from_200sma: The opening price relative to the 200-day simple moving average.
- sigma_ratio_open_from_20sma: The ratio of standard deviation to the 20-day simple moving average at the open.
- consecutive_days_above_20sma: The number of consecutive days the stock has been above the 20-day simple moving average.
- open_from_BB_up: The opening price relative to the upper Bollinger Band.
- open_from_BB_down: The opening price relative to the lower Bollinger Band.
- 1month_rolling_max: The highest price over the past month.
- 1month_change_from_high: The change from the highest price over the past month.
- 1month_change_from_high_at_open: The change from the highest price over the past month at the open.
- 3month_change_from_high: The change from the highest price over the past three months.
- 6month_change_from_high: The change from the highest price over the past six months.
- red_days: The number of days the stock closed lower than it opened.
- green_days: The number of days the stock closed higher than it opened.
- pm_dollar_volume: The dollar volume of shares traded during pre-market trading.
- first_15min_move: The price movement during the first 15 minutes of trading.
- first_15min_max_up: The maximum upward movement during the first 15 minutes.
- first_15min_max_down: The maximum downward movement during the first 15 minutes.
- first_15min_volume: The volume of shares traded during the first 15 minutes.
- first_15_min_relative_volume: The relative volume during the first 15 minutes.
- first_hour_move: The price movement during the first hour of trading.
- first_hour_max_up: The maximum upward movement during the first hour.
- first_hour_max_down: The maximum downward movement during the first hour.
- first_hour_volume: The volume of shares traded during the first hour.
- first_hour_relative_volume: The relative volume during the first hour.
- open_to_close_move: The price movement from open to close.
- open_to_close_max_up: The maximum upward movement from open to close.
- open_to_close_max_down: The maximum downward movement from open to close.
- open_to_close_volume: The volume of shares traded from open to close.
- open_to_close_relative_volume: The relative volume from open to close.
- power_hour_move: The price movement during the last hour of trading.
- power_hour_max_up: The maximum upward movement during the last hour.
- power_hour_max_down: The maximum downward movement during the last hour.
- power_hour_volume: The volume of shares traded during the last hour.
- power_hour_relative_volume: The relative volume during the last hour.
- first_hour_to_close_move: The price movement from the first hour to close.
- first_hour_to_close_max_up: The maximum upward movement from the first hour to close.
- first_hour_to_close_max_down: The maximum downward movement from the first hour to close.
- first_hour_to_close_volume: The volume of shares traded from the first hour to close.
- first_hour_to_close_relative_volume: The relative volume from the first hour to close.
- first_hour_to_power_hour_move: The price movement from the first hour to the last hour.
- first_hour_to_power_hour_max_up: The maximum upward movement from the first hour to the last hour.
- first_hour_to_power_hour_max_down: The maximum downward movement from the first hour to the last hour.
- first_hour_to_power_hour_volume: The volume of shares traded from the first hour to the last hour.
- first_hour_to_power_hour_relative_volume: The relative volume from the first hour to the last hour.
- open_to_power_hour_move: The price movement from open to the last hour.
- open_to_power_hour_max_up: The maximum upward movement from open to the last hour.
- open_to_power_hour_max_down: The maximum downward movement from open to the last hour.
- open_to_power_hour_volume: The volume of shares traded from open to the last hour.
- open_to_power_hour_relative_volume: The relative volume from open to the last hour.
- duration_before_breakout_of_pm_high: The time duration before breaking out of the pre-market high.
- move_from_breakout_of_pm_high: The price movement after breaking out of the pre-market high.
- lower_move_before_breakout_of_pm_high: The lower price movement before breaking out of the pre-market high.
- duration_below_open: The time duration the stock stayed below the opening price.
- duration_below_9ema: The time duration the stock stayed below the 9-day exponential moving average.
- duration_below_9ema_first_hour: The time duration the stock stayed below the 9-day exponential moving average during the first hour.
- duration_below_20ema: The time duration the stock stayed below the 20-day exponential moving average.
- duration_below_20ema_first_hour: The time duration the stock stayed below the 20-day exponential moving average during the first hour.
- duration_below_vwap: The time duration the stock stayed below the volume-weighted average price.
- duration_below_vwap_first_hour: The time duration the stock stayed below the volume-weighted average price during the first hour.
- number_of_red_candles_one_hour_before_open: The number of red candles one hour before the open.
- percent_of_red_candles_one_hour_before_open: The percentage of red candles one hour before the open.
- number_of_red_candles_one_hour_after_open: The number of red candles one hour after the open.
- percent_of_red_candles_one_hour_after_open: The percentage of red candles one hour after the open.
- number_of_red_candles_during_open: The number of red candles during the open.
- percent_of_red_candles_during_open: The percentage of red candles during the open.
- from_pm_high_to_open: The price movement from the pre-market high to the open.
- pm_high_vs_high: The comparison between the pre-market high and the session high.
- pm_retracement: The retracement from the pre-market high.
- break_200sma: The event of breaking the 200-day simple moving average.
- test_of_pm_high: The test of the pre-market high.
- days_til_next_earnings: The number of days until the next earnings report.
- eps_diff_percent: The percentage difference in earnings per share.
- revenue_diff_percent: The percentage difference in revenue.


