import pandas as pd
import numpy as np
import math


# Read in the CSV file as a Pandas DataFrame
df = pd.read_csv(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\full.csv')

# appliquer un filtre
df = df[df['market_cap']>1000000000]

# ne conserver que certaines colonnes
#df_filtered = df[['ticker','green_days','red_days','first_hour_max_down','first_hour_max_up','first_hour_move','from_pm_high_to_open','gap','market_cap','number_of_red_candles_one_hour_before_open','percent_of_red_candles_one_hour_before_open','pm_float_rotation','pm_retracement','pm_volume','sigma_percent']]
df_filtered = df[['ticker','open','above_20sma','green_days','red_days','first_hour_max_down','first_hour_move','first_hour_max_up','from_pm_high_to_open','gap','market_cap','number_of_red_candles_one_hour_before_open','percent_of_red_candles_one_hour_before_open','pm_float_rotation','pm_volume','sigma_percent']]

# ne conserver que les lignes qui n'ont pas de na pour ces colonnes
df_filtered.replace('na', np.nan, inplace=True)
df_filtered = df_filtered.dropna(subset=['first_hour_max_up','first_hour_max_down','above_20sma','green_days','red_days'])

# Calculate strat
def compare(row):
    if float(row['first_hour_max_up']) < 0.01 and float(row['first_hour_max_down']) < -0.02:
        return True
    else:
        return False

df_filtered['strat1'] = df_filtered.apply(compare, axis=1)

# calcule le volume en dollars ---------------------------------------------
# supprime les espaces parce que j'en avais mis sans faire exprès dans le csv
df['pm_volume'] = df['pm_volume'].str.replace(' ', '')
def pm_dolls(row):
    if row['pm_volume'] == ' na' or math.isnan(float(row['pm_volume'])) or math.isnan(float(row['open'])) :
        return 'NaN'
    else:
        return float(row['pm_volume'])*float(row['open'])
df_filtered['pm_dollar_volume'] = df_filtered.apply(pm_dolls, axis=1) # à supprimer au prochain run du data_retriever


df_filtered = df_filtered.drop(['first_hour_max_up', 'pm_volume','open'], axis=1)

# génère un sample aléatoire de 50%
sampled_df = df_filtered
#sampled_df = df_filtered.sample(frac=0.5, random_state=42)
#rest_part_50 = df.drop(sampled_df.index)

pd.set_option('display.max_columns', None)
print(sampled_df.head(40))
print(sampled_df.shape)

# Save the modified DataFrame back to the CSV file
sampled_df.to_csv(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\strat3s.csv', index=False)





# ##################################################################################################
# ##################################################################################################








# display all unique values
#print(df['pm_volume'].unique())
