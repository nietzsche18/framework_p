import pandas as pd
import math


# Read in the CSV file as a Pandas DataFrame
df = pd.read_csv(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\full.csv')

# appliquer un filtre
df = df[df['market_cap']>1000000000]

# ne conserver que certaines colonnes
#df_filtered = df[['ticker','green_days','red_days','first_hour_max_down','first_hour_max_up','first_hour_move','from_pm_high_to_open','gap','market_cap','number_of_red_candles_one_hour_before_open','percent_of_red_candles_one_hour_before_open','pm_float_rotation','pm_retracement','pm_volume','sigma_percent']]
df_filtered = df[['ticker','open','above_20sma','above_50sma','green_days','red_days','first_hour_max_down','first_hour_max_up','from_pm_high_to_open','gap','market_cap','number_of_red_candles_one_hour_before_open','percent_of_red_candles_one_hour_before_open','pm_float_rotation','pm_volume','sigma_percent']]

# Keep only rows where column A contains numeric values
df_filtered = df_filtered[pd.to_numeric(df_filtered['first_hour_max_up'], errors='coerce').notnull()]
df_filtered = df_filtered[pd.to_numeric(df_filtered['first_hour_max_down'], errors='coerce').notnull()]


# Calculate if column A is above column B
def compare(row):
    if float(row['first_hour_max_up']) > 0.015 and float(row['first_hour_max_down']) > -0.01:
        return True
    else:
        return False

df_filtered['strat1'] = df_filtered.apply(compare, axis=1)

df['pm_volume'] = df['pm_volume'].str.replace(' ', '')

def pm_dolls(row):
    if row['pm_volume'] == ' na' or math.isnan(float(row['pm_volume'])) or math.isnan(float(row['open'])) :
        return 'NaN'
    else:
        return float(row['pm_volume'])*float(row['open'])

df_filtered['pm_dollar_volume'] = df_filtered.apply(pm_dolls, axis=1)

df_filtered = df_filtered.drop(['first_hour_max_down', 'first_hour_max_up', 'pm_volume'], axis=1)

sampled_df = df_filtered.sample(frac=0.5, random_state=42)

pd.set_option('display.max_columns', None)
print(sampled_df.head(40))
print(sampled_df.shape)

# Save the modified DataFrame back to the CSV file
sampled_df.to_csv(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\strat1.csv', index=False)





# ##################################################################################################
# ##################################################################################################








# display all unique values
#print(df['pm_volume'].unique())
