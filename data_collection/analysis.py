
#coding: utf-8
#source activate py38


import pandas
import fin_functions
from datetime import datetime
import matplotlib.pyplot as plt
import mplfinance as mpl
import math
import pytz


def low_tf(day_date, ticker, average_volume, gap, previous_day_close, sma200):

    data = fin_functions.get_5min_data(ticker, day_date)
    df_low_tf = pandas.DataFrame.from_records(data)
    df_low_tf['9ema'] = df_low_tf['c'].ewm(span=9, adjust=False).mean()
    df_low_tf['20ema'] = df_low_tf['c'].ewm(span=20, adjust=False).mean()

    tz = pytz.timezone('America/New_York') # Specify the timezone you want to convert to
    df_low_tf['t'] = df_low_tf['t'] / 1000
    def convert_timezone(timestamp):
        # Convert the timestamp to a datetime object in UTC
        utc_datetime = datetime.utcfromtimestamp(timestamp)

        # Convert the datetime object to the desired timezone, taking DST into account
        local_datetime = tz.normalize(pytz.utc.localize(utc_datetime).astimezone(tz))

        # Format the date string in the desired format
        date_str = local_datetime.strftime('%Y-%m-%d %H:%M:%S') # '%Y-%m-%d %H:%M:%S %Z%z' pour avoir la timezone

        return date_str
    df_low_tf['t'] = df_low_tf['t'].apply(convert_timezone)

    #open: 09:30 (66/191)
    # pm commence à 9h heure FR et 4h heure de NY
    """
    with pandas.option_context('display.max_rows', None, 'display.max_columns', None):  # permet d'afficher toutes les lignes & colonnes more options can be specified also
        print(df_low_tf)
    """

    # calcul vwap
    df_low_tf['vwap'] = (df_low_tf['v']*(df_low_tf['h']+df_low_tf['l'])/2).cumsum() / df_low_tf['v'].cumsum()

    # index de l'open en fait
    index_of_pm = df_low_tf.index[df_low_tf['t'] == day_date + " 09:30:00"]
    index_of_first_hour = df_low_tf.index[df_low_tf['t'] == day_date + " 10:30:00"]
    index_of_first_15m = df_low_tf.index[df_low_tf['t'] == day_date + " 09:45:00"]
    index_of_close = df_low_tf.index[df_low_tf['t'] == day_date + " 15:55:00"] + 1 # last candle
    index_of_power_hour = df_low_tf.index[df_low_tf['t'] == day_date + " 15:00:00"]

    break_200sma = 'na'
    pm_high = 'na'
    pm_volume = 'na'
    first_15min_move = 'na'
    first_15min_max_up = 'na'
    first_15min_max_down = 'na'
    first_15min_volume = 'na'
    first_15_min_relative_volume = 'na'
    first_hour_move = 'na'
    first_hour_volume = 'na'
    first_hour_relative_volume = 'na'
    number_of_red_candles_one_hour_before_open = 'na'
    percent_of_red_candles_one_hour_before_open = 'na'
    number_of_red_candles_one_hour_after_open = 'na'
    percent_of_red_candles_one_hour_after_open = 'na'
    from_pm_high_to_open = 'na'
    day_open = 'na'

    duration_below_9ema_first_hour = 'na'
    duration_below_20ema_first_hour = 'na'
    duration_below_vwap_first_hour = 'na'

    pm_retracement = 'na'

    open_to_close_move = 'na'
    open_to_close_max_up = 'na'
    open_to_close_max_down = 'na'
    open_to_close_volume = 'na'
    open_to_close_relative_volume = 'na'

    first_hour_move = 'na'
    first_hour_max_up = 'na'
    first_hour_max_down = 'na'
    first_hour_volume = 'na'
    first_hour_relative_volume = 'na'

    # On vérifie qu'il y a bien une ligne qui commence à 9h30 pour pouvoir distinguer le prémarket
    if index_of_pm.size != 0 :
        day_open = float(df_low_tf['o'][index_of_pm])
        break_200sma = True if day_open > sma200 > previous_day_close else False

        # data first_15min
        if index_of_first_15m.size != 0:
            # A NOTER : quand on prend la valeur il faut décaler de -1 mais pas quand on prend le dataframe (wtf)
            first_15min_move = (df_low_tf['c'][index_of_first_15m[0]-1] - df_low_tf['o'][index_of_pm[0]])/df_low_tf['o'][index_of_pm[0]]
            first_15min_max_up = df_low_tf['h'][index_of_pm[0]:index_of_first_15m[0]].max()/df_low_tf['o'][index_of_pm[0]]-1
            first_15min_max_down = df_low_tf['l'][index_of_pm[0]:index_of_first_15m[0]].min()/df_low_tf['o'][index_of_pm[0]]-1
            first_15min_volume = df_low_tf['v'][index_of_pm[0]:index_of_first_15m[0]].sum()
            first_15_min_relative_volume = first_15min_volume / average_volume

        # data first_hour
        if index_of_first_hour.size != 0:
            first_hour_move = (df_low_tf['c'][index_of_first_hour[0]-1] - df_low_tf['o'][index_of_pm[0]])/df_low_tf['o'][index_of_pm[0]]
            first_hour_max_up = df_low_tf['h'][index_of_pm[0]:index_of_first_hour[0]].max()/df_low_tf['o'][index_of_pm[0]]-1
            first_hour_max_down = df_low_tf['l'][index_of_pm[0]:index_of_first_hour[0]].min()/df_low_tf['o'][index_of_pm[0]]-1
            first_hour_volume = df_low_tf['v'].iloc[index_of_pm[0]:index_of_first_hour[0]].sum()
            first_hour_relative_volume = first_hour_volume / average_volume

            df_first_hour = df_low_tf.iloc[index_of_pm[0]:index_of_first_hour[0]]
            number_of_red_candles_one_hour_after_open = df_first_hour[df_first_hour['c'] < df_first_hour['o']]['c'].count()
            percent_of_red_candles_one_hour_after_open = number_of_red_candles_one_hour_after_open / df_first_hour['c'].count()

            duration_below_9ema_first_hour = 0
            for index, row in df_first_hour.iterrows():
                if (row['c'] < row['9ema']):
                    duration_below_9ema_first_hour = duration_below_9ema_first_hour + 5

            duration_below_20ema_first_hour = 0
            for index, row in df_first_hour.iterrows():
                if (row['c'] < row['20ema']):
                    duration_below_20ema_first_hour = duration_below_20ema_first_hour + 5

            duration_below_vwap_first_hour = 0
            for index, row in df_first_hour.iterrows():
                if (row['c'] < row['vwap']):
                    duration_below_vwap_first_hour = duration_below_vwap_first_hour + 5

        # si prémarket existe ...
        if index_of_pm[0] != 0:
            pm_high = df_low_tf['h'].iloc[0:index_of_pm[0]].max()
            pm_volume = df_low_tf['v'].iloc[0:index_of_pm[0]].sum()
            from_pm_high_to_open = (df_low_tf['o'][index_of_pm[0]] - pm_high) / pm_high
            df_pm = df_low_tf.iloc[:index_of_pm[0]]
            number_of_red_candles_one_hour_before_open = df_pm[df_pm['c'] < df_pm['o']]['c'].count()
            percent_of_red_candles_one_hour_before_open = number_of_red_candles_one_hour_before_open / df_pm['c'].count()

            if not math.isnan(gap) and index_of_first_hour.size != 0 and pm_high != previous_day_close :
                pm_retracement = (pm_high - day_open)/(pm_high - previous_day_close)

        # data open_to_close
        if index_of_close.size != 0:
            open_to_close_move = (df_low_tf['c'][index_of_close[0]-1] - df_low_tf['o'][index_of_pm[0]])/df_low_tf['o'][index_of_pm[0]]
            open_to_close_max_up = df_low_tf['h'][index_of_pm[0]:index_of_close[0]].max()/df_low_tf['o'][index_of_pm[0]]-1
            open_to_close_max_down = df_low_tf['l'][index_of_pm[0]:index_of_close[0]].min()/df_low_tf['o'][index_of_pm[0]]-1
            open_to_close_volume = df_low_tf['v'].iloc[index_of_pm[0]:index_of_close[0]].sum()
            open_to_close_relative_volume = open_to_close_volume / average_volume


    # ----- PREMARKET analysis, red candles, durations -----
    after_first_hour = 'na'
    breakout_time = 0
    duration_before_breakout_of_pm_high = None
    move_from_breakout_of_pm_high = None
    lower_move_before_breakout_of_pm_high = None
    number_of_red_candles_during_open = 'na'
    percent_of_red_candles_during_open = 'na'

    pm_high_vs_high = 'na'

    duration_below_open = 'na'
    duration_below_9ema = 'na'
    duration_below_20ema = 'na'
    duration_below_vwap = 'na'

    test_of_pm_high = 'na'

    if index_of_close.size != 0 and index_of_pm.size != 0 :

        df_low_tf_during_open = df_low_tf.iloc[index_of_pm[0]:index_of_close[0]]
        number_of_red_candles_during_open = df_low_tf_during_open[df_low_tf_during_open['c'] < df_low_tf_during_open['o']]['c'].count()
        percent_of_red_candles_during_open = number_of_red_candles_during_open / df_low_tf_during_open['c'].count()

        # il se peut que les données commencent à 9h30, donc ici on met tous les calculs qui ne concernent qu'un éventuel pré-market
        if index_of_pm[0] != 0:
            pm_high_vs_high = (df_low_tf_during_open['h'].max() - pm_high) / pm_high

            # dataframe avec données au dessus du pm_high pendant l'open
            df_above_pm_high_since_open = df_low_tf_during_open[df_low_tf_during_open['h'] > pm_high ]

            if not df_above_pm_high_since_open.empty:
                breakout_datetime = df_above_pm_high_since_open['t'].iat[0] # donne l'heure du breakout du pm_high
                open_time = datetime.strptime(day_date + " 09:30:00",  '%Y-%m-%d %H:%M:%S')
                breakout_datetime = datetime.strptime(breakout_datetime,  '%Y-%m-%d %H:%M:%S')
                duration_before_breakout_of_pm_high = breakout_datetime - open_time
                index_of_breakout = df_low_tf_during_open.index[df_low_tf_during_open['t'] == breakout_datetime.strftime("%Y-%m-%d %H:%M:%S")].tolist()[0]
                move_from_breakout_of_pm_high = (df_low_tf['c'][index_of_close[0]-1] - df_low_tf_during_open['c'][index_of_breakout])/df_low_tf['o'][index_of_pm[0]]
                low_before_breakout_of_pm_high = df_low_tf_during_open.iloc[:index_of_breakout]['l'].min()

                lower_move_before_breakout_of_pm_high = 0
                if not math.isnan(low_before_breakout_of_pm_high):
                    lower_move_before_breakout_of_pm_high = low_before_breakout_of_pm_high / df_low_tf_during_open['o'].iat[0] -1

            if abs((pm_high-df_low_tf_during_open['h'].max())/pm_high)<0.01:
                test_of_pm_high = True
            else:
                test_of_pm_high = False

        duration_below_open = 0
        for index, row in df_low_tf_during_open.iterrows():
            if (row['c'] < df_low_tf['o'][index_of_pm[0]]):
                duration_below_open = duration_below_open + 5
            else:
                break

        duration_below_9ema = 0
        for index, row in df_low_tf_during_open.iterrows():
            if (row['c'] < row['9ema']):
                duration_below_9ema = duration_below_9ema + 5

        duration_below_20ema = 0
        for index, row in df_low_tf_during_open.iterrows():
            if (row['c'] < row['20ema']):
                duration_below_20ema = duration_below_20ema + 5

        duration_below_vwap = 0
        for index, row in df_low_tf_during_open.iterrows():
            if (row['c'] < row['vwap']):
                duration_below_vwap = duration_below_vwap + 5

    # ---- POWER HOUR -----

    power_hour_move = 'na'
    power_hour_max_up = 'na'
    power_hour_max_down = 'na'
    power_hour_volume = 'na'
    power_hour_relative_volume = 'na'

    if index_of_power_hour.size != 0 and index_of_close.size != 0 :
        power_hour_move = (df_low_tf['c'][index_of_close[0]-1] - df_low_tf['o'][index_of_power_hour[0]])/df_low_tf['o'][index_of_power_hour[0]]
        power_hour_max_up = df_low_tf['h'][index_of_power_hour[0]:index_of_close[0]].max()/df_low_tf['o'][index_of_power_hour[0]]-1
        power_hour_max_down = df_low_tf['l'][index_of_power_hour[0]:index_of_close[0]].min()/df_low_tf['o'][index_of_power_hour[0]]-1
        power_hour_volume = df_low_tf['v'].iloc[index_of_power_hour[0]:index_of_close[0]].sum()
        power_hour_relative_volume = power_hour_volume / average_volume



    # ---- FIRST HOUR TO CLOSE -----

    first_hour_to_close_move = 'na'
    first_hour_to_close_max_up = 'na'
    first_hour_to_close_max_down = 'na'
    first_hour_to_close_volume = 'na'
    first_hour_to_close_relative_volume = 'na'

    if index_of_first_hour.size != 0 and index_of_close.size != 0 :
        first_hour_to_close_move = (df_low_tf['c'][index_of_close[0]-1] - df_low_tf['o'][index_of_first_hour[0]])/df_low_tf['o'][index_of_first_hour[0]]
        first_hour_to_close_max_up = df_low_tf['h'][index_of_first_hour[0]:index_of_close[0]].max()/df_low_tf['o'][index_of_first_hour[0]]-1
        first_hour_to_close_max_down = df_low_tf['l'][index_of_first_hour[0]:index_of_close[0]].min()/df_low_tf['o'][index_of_first_hour[0]]-1
        first_hour_to_close_volume = df_low_tf['v'].iloc[index_of_first_hour[0]:index_of_close[0]].sum()
        first_hour_to_close_relative_volume = first_hour_to_close_volume / average_volume



    # ---- FIRST HOUR TO POWER HOUR -----

    first_hour_to_power_hour_move = 'na'
    first_hour_to_power_hour_max_up = 'na'
    first_hour_to_power_hour_max_down = 'na'
    first_hour_to_power_hour_volume = 'na'
    first_hour_to_power_hour_relative_volume = 'na'

    if index_of_first_hour.size != 0 and index_of_power_hour.size != 0 :
        first_hour_to_power_hour_move = (df_low_tf['c'][index_of_power_hour[0]-1] - df_low_tf['o'][index_of_first_hour[0]])/df_low_tf['o'][index_of_first_hour[0]]
        first_hour_to_power_hour_max_up = df_low_tf['h'][index_of_first_hour[0]:index_of_power_hour[0]].max()/df_low_tf['o'][index_of_first_hour[0]]-1
        first_hour_to_power_hour_max_down = df_low_tf['l'][index_of_first_hour[0]:index_of_power_hour[0]].min()/df_low_tf['o'][index_of_first_hour[0]]-1
        first_hour_to_power_hour_volume = df_low_tf['v'].iloc[index_of_first_hour[0]:index_of_power_hour[0]].sum()
        first_hour_to_power_hour_relative_volume = first_hour_to_power_hour_volume / average_volume

    # ---- OPEN TO POWER HOUR -----

    open_to_power_hour_move = 'na'
    open_to_power_hour_max_up = 'na'
    open_to_power_hour_max_down = 'na'
    open_to_power_hour_volume = 'na'
    open_to_power_hour_relative_volume = 'na'

    if index_of_pm.size != 0 and index_of_power_hour.size != 0 :
        open_to_power_hour_move = (df_low_tf['c'][index_of_power_hour[0]-1] - df_low_tf['o'][index_of_pm[0]])/df_low_tf['o'][index_of_pm[0]]
        open_to_power_hour_max_up = df_low_tf['h'][index_of_pm[0]:index_of_power_hour[0]].max()/df_low_tf['o'][index_of_pm[0]]-1
        open_to_power_hour_max_down = df_low_tf['l'][index_of_pm[0]:index_of_power_hour[0]].min()/df_low_tf['o'][index_of_pm[0]]-1
        open_to_power_hour_volume = df_low_tf['v'].iloc[index_of_pm[0]:index_of_power_hour[0]].sum()
        open_to_power_hour_relative_volume = open_to_power_hour_volume / average_volume


    return pm_volume, first_15min_move, first_15min_max_up, first_15min_max_down, first_15min_volume, first_15_min_relative_volume, first_hour_move, first_hour_max_up, first_hour_max_down, first_hour_volume, first_hour_relative_volume, open_to_close_move, open_to_close_max_up, open_to_close_max_down, open_to_close_volume, open_to_close_relative_volume, power_hour_move, power_hour_max_up, power_hour_max_down, power_hour_volume, power_hour_relative_volume, first_hour_to_close_move, first_hour_to_close_max_up, first_hour_to_close_max_down, first_hour_to_close_volume, first_hour_to_close_relative_volume, first_hour_to_power_hour_move, first_hour_to_power_hour_max_up, first_hour_to_power_hour_max_down, first_hour_to_power_hour_volume, first_hour_to_power_hour_relative_volume, open_to_power_hour_move, open_to_power_hour_max_up, open_to_power_hour_max_down, open_to_power_hour_volume, open_to_power_hour_relative_volume, duration_before_breakout_of_pm_high, move_from_breakout_of_pm_high, lower_move_before_breakout_of_pm_high, duration_below_open, duration_below_9ema, duration_below_9ema_first_hour, duration_below_20ema, duration_below_20ema_first_hour, duration_below_vwap, duration_below_vwap_first_hour, number_of_red_candles_one_hour_before_open, percent_of_red_candles_one_hour_before_open, number_of_red_candles_one_hour_after_open, percent_of_red_candles_one_hour_after_open, number_of_red_candles_during_open, percent_of_red_candles_during_open, from_pm_high_to_open, pm_high_vs_high, pm_retracement, break_200sma, test_of_pm_high


def show_df(df):
    df_to_show = df
    df_to_show['Date'] = pandas.to_datetime(df_to_show['t'])
    df_to_show.set_index('Date', inplace=True)
    df_to_show = df_to_show[['o','h','l','c']]
    df_to_show.rename(columns={"o": "Open", "h": "High", "l":"Low", "c":"Close"}, inplace=True)
    #print(df_to_show)
    mpl.plot(
        df_to_show,
        type="candle"
    )









#
