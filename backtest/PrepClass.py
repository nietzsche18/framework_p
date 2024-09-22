#coding: utf-8
#source activate py38

import numpy as np
import math
from typing import List

'''
This class prepares the data for each strategy.
For each new strategy, you need to:
    - adapt the variables (filters, inputs, drop_na, to_drop)
    - add the filters if they are not present (filter_function)
    - add the calculation of the data to predict (to_predict_function)
    - adapt the returns (returns_function)
'''

full_dtypes = {
    'above_20sma': "bool",
    'ticker': "category",
    'from_pm_high_to_open': "float64",
    'number_of_red_candles_one_hour_before_open': "float64",
    'percent_of_red_candles_one_hour_before_open': "float64",
    'green_days': "int64",
    'red_days': "int64",
    'pm_float_rotation': "float64",
    'pm_dollar_volume': "float64"
}

class Prepare:
    def __init__(self, df, name: str, filters: List[str], inputs: List[str], drop_na: List[str], to_drop: List[str]):
        self.df = df
        self.name = name
        self.filters = filters
        self.inputs = inputs # liste des colonnes à conserver à partir de full
        self.drop_na = drop_na
        self.to_drop = to_drop
        self.data = None # df ready
        self.initialize()

    def initialize(self):
        print("Preparing data for ", self.name)
        df = self.df
        # Read in the CSV file as a Pandas DataFrame
        #print(df['to_predict'].isna().sum())
        df = filter_function(df, self.filters)
        df_filtered = df[self.inputs]
        df_filtered.replace('na', np.nan, inplace=True)
        df_filtered.replace('', np.nan, inplace=True)
        dtypes = get_dtype(df_filtered)
        df_filtered = df_filtered.astype(dtypes)
        df_filtered = df_filtered.dropna(subset=self.drop_na) # certaines colonnes comportent de nombreux na et risquent de fausser les trainings
        df_filtered['to_predict'] = df_filtered.apply(lambda row: to_predict_function(row, self.name), axis=1)
        df_filtered['returns'] = df_filtered.apply(lambda row: returns_function(row, self.name), axis=1)
        df_filtered = df_filtered.drop(self.to_drop, axis=1)
        self.data = df_filtered
        print('Data ready for ', self.name)


# Apply some global filters
def filter_function(df, filters):
    filtered_df = df
    for filter in filters:
        if filter == 'market_cap>100b':
            filtered_df = filtered_df[filtered_df['market_cap']>1000000000]
        if filter == 'average_volume>10mUSD':
            filtered_df = filtered_df[filtered_df['average_dollar_volume_previous_day']>10000000]
    return filtered_df


# Prepare the data that will need to be predicted
def to_predict_function(row, strat):
    if strat == 'strat1' :
        if float(row['first_hour_max_up']) > 0.01 and float(row['first_hour_max_down']) > -0.01:
            return True
        else:
            return False

    elif strat =='strat1_percentile':
        if float(row['first_hour_max_up']) > 0.01 and float(row['first_hour_max_down']) > -0.01:
            return True
        else:
            return False

    elif strat =='strat1_percentile_open_to_close':
        if float(row['open_to_close_max_up']) > 0.01 and float(row['open_to_close_max_down']) > -0.01:
            return True
        else:
            return False

    elif strat == 'strat2':
        if float(row['first_hour_max_up']) > 0.015 and float(row['first_hour_max_down']) > -0.01:
            return True
        else:
            return False

    elif strat == 'strat3':
        if float(row['first_hour_max_up']) > 0.02 and float(row['first_hour_max_down']) > -0.01:
            return True
        else:
            return False

    elif strat == 'strat1_s':
        if float(row['first_hour_max_up']) < 0.01 and float(row['first_hour_max_down']) < -0.01:
            return True
        else:
            return False

    elif strat == 'strat2_s':
        if float(row['first_hour_max_up']) < 0.01 and float(row['first_hour_max_down']) < -0.015:
            return True
        else:
            return False

    elif strat == 'strat3_s':
        if float(row['first_hour_max_up']) < 0.01 and float(row['first_hour_max_down']) < -0.02:
            return True
        else:
            return False

    else:
        print('Missing strategy in to_predict_function')

# Calculates return
def returns_function(row, strat):
    if strat == 'strat1':
        if float(row['first_hour_max_down']) < -0.01:
            return float(0.99)
        elif float(row['first_hour_max_up']) > 0.01:
            return float(1.01)
        else:
            return (1+float(row['first_hour_move']))

    elif strat == 'strat1_percentile':
        if float(row['first_hour_max_down']) < -0.01:
            return float(0.99)
        elif float(row['first_hour_max_up']) > 0.01:
            return float(1.01)
        else:
            return (1+float(row['first_hour_move']))

    elif strat == 'strat1_percentile_open_to_close':
        if float(row['open_to_close_max_down']) < -0.01:
            return float(0.99)
        elif float(row['open_to_close_max_up']) > 0.01:
            return float(1.01)
        else:
            return (1+float(row['open_to_close_move']))

    elif strat == 'strat2':
        if float(row['first_hour_max_down']) < -0.01:
            return float(0.99)
        elif float(row['first_hour_max_up']) > 0.015:
            return float(1.015)
        else:
            return (1+float(row['first_hour_move']))

    elif strat == 'strat3':
        if float(row['first_hour_max_down']) < -0.01:
            return float(0.99)
        elif float(row['first_hour_max_up']) > 0.02:
            return float(1.02)
        else:
            return (1+float(row['first_hour_move']))

    elif strat == 'strat1_s':
        if float(row['first_hour_max_up']) > 0.01:
            return float(0.99)
        elif float(row['first_hour_max_down']) < -0.01:
            return float(1.01)
        else:
            return (1+float(row['first_hour_move']))

    elif strat == 'strat2_s':
        if float(row['first_hour_max_up']) > 0.01:
            return float(0.99)
        elif float(row['first_hour_max_down']) < -0.015:
            return float(1.015)
        else:
            return (1+float(row['first_hour_move']))

    elif strat == 'strat3_s':
        if float(row['first_hour_max_up']) > 0.01:
            return float(0.99)
        elif float(row['first_hour_max_down']) < -0.02:
            return float(1.02)
        else:
            return (1+float(row['first_hour_move']))


    else:
        print('Missing strategy in returns_function')


def get_dtype(df):
    column_names = df.columns.tolist()
    filtered_dict = {key: value for key, value in full_dtypes.items() if key in column_names}
    return filtered_dict








#
