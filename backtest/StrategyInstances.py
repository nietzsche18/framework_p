#coding: utf-8
#source activate py38

from StrategyClass import Strategy

# name, description, filters, inputs, drop_na, to_drop, models, model_type

# possible d'ajouter les above_20sma, above_50sma, above_200sma quand dispo
"""
strat1 = Strategy("strat1",
     "max_up > 1%; max_down > -1% ; first hour (RR 1:1)",
     ['market_cap>100b'],
     ['ticker','date','green_days','red_days','first_hour_max_down','first_hour_move','first_hour_max_up','from_pm_high_to_open','gap','market_cap','number_of_red_candles_one_hour_before_open','percent_of_red_candles_one_hour_before_open','pm_float_rotation','pm_dollar_volume','sigma_percent'],
     ['first_hour_max_up','first_hour_max_down','green_days','red_days'],
     ['first_hour_move', 'first_hour_max_up', 'first_hour_max_down'],
     ['xgboost'],
     "classification"
     )

strat2 = Strategy("strat2",
     "max_up > 1.5%; max_down > -1% ; first hour (RR 1.5:1)",
     ['market_cap>100b'],
     ['ticker','date','green_days','red_days','first_hour_max_down','first_hour_move','first_hour_max_up','from_pm_high_to_open','gap','market_cap','number_of_red_candles_one_hour_before_open','percent_of_red_candles_one_hour_before_open','pm_float_rotation','pm_dollar_volume','sigma_percent'],
     ['first_hour_max_up','first_hour_max_down','green_days','red_days'],
     ['first_hour_move', 'first_hour_max_up', 'first_hour_max_down'],
     ['xgboost'],
     "classification"
     )

strat3 = Strategy("strat3",
     "max_up > 2%; max_down > -1% ; first hour (RR 2:1)",
     ['market_cap>100b'],
     ['ticker','date','green_days','red_days','first_hour_max_down','first_hour_move','first_hour_max_up','from_pm_high_to_open','gap','market_cap','number_of_red_candles_one_hour_before_open','percent_of_red_candles_one_hour_before_open','pm_float_rotation','pm_dollar_volume','sigma_percent'],
     ['first_hour_max_up','first_hour_max_down','green_days','red_days'],
     ['first_hour_move', 'first_hour_max_up', 'first_hour_max_down'],
     ['xgboost'],
     "classification"
     )

strat1_s = Strategy("strat1_s",
     "max_up < 1%; max_down < -1% ; first hour (RR 1:1)",
     ['market_cap>100b'],
     ['ticker','date','green_days','red_days','first_hour_max_down','first_hour_move','first_hour_max_up','from_pm_high_to_open','gap','market_cap','number_of_red_candles_one_hour_before_open','percent_of_red_candles_one_hour_before_open','pm_float_rotation','pm_dollar_volume','sigma_percent'],
     ['first_hour_max_up','first_hour_max_down','green_days','red_days'],
     ['first_hour_move', 'first_hour_max_up', 'first_hour_max_down'],
     ['xgboost'],
     "classification"
     )

strat2_s = Strategy("strat2_s",
     "max_up < 1.5%; max_down < -1% ; first hour (RR 1.5:1)",
     ['market_cap>100b'],
     ['ticker','date','green_days','red_days','first_hour_max_down','first_hour_move','first_hour_max_up','from_pm_high_to_open','gap','market_cap','number_of_red_candles_one_hour_before_open','percent_of_red_candles_one_hour_before_open','pm_float_rotation','pm_dollar_volume','sigma_percent'],
     ['first_hour_max_up','first_hour_max_down','green_days','red_days'],
     ['first_hour_move', 'first_hour_max_up', 'first_hour_max_down'],
     ['xgboost'],
     "classification"
     )

strat3_s = Strategy("strat3_s",
     "max_up < 2%; max_down < -1% ; first hour (RR 2:1)",
     ['market_cap>100b'],
     ['ticker','date','green_days','red_days','first_hour_max_down','first_hour_move','first_hour_max_up','from_pm_high_to_open','gap','market_cap','number_of_red_candles_one_hour_before_open','percent_of_red_candles_one_hour_before_open','pm_float_rotation','pm_dollar_volume','sigma_percent'],
     ['first_hour_max_up','first_hour_max_down','green_days','red_days'],
     ['first_hour_move', 'first_hour_max_up', 'first_hour_max_down'],
     ['xgboost'],
     "classification"
     )
"""
strat1_percentile = Strategy("strat1_percentile",
     "max_up < 2%; max_down < -1% ; first hour (RR 2:1)",
     ['market_cap>100b'],
     ['ticker','date','first_hour_max_down','first_hour_move','first_hour_max_up','open_from_BB_up_percentile','x_day_high_at_open_percentile','1month_change_from_high_percentile','gap_percentile','pm_dollar_volume_percentile'],
     ['first_hour_max_up','first_hour_max_down','green_days_percentile','red_days_percentile'],
     ['first_hour_move', 'first_hour_max_up', 'first_hour_max_down'],
     ['xgboost'],
     "classification"
     )

#strategy_list = [strat1, strat2, strat3, strat1_s, strat2_s, strat3_s]
strategy_list = [strat1_percentile]
