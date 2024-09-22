import pandas as pd

import math

# Read in the CSV file as a Pandas DataFrame
df = pd.read_csv(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\full.csv')

df['pm_volume'] = df['pm_volume'].str.replace(' ', '')
def pm_dolls(row):
    if row['pm_volume'] == ' na' or row['pm_volume'] == 'na' or math.isnan(float(row['pm_volume'])) or math.isnan(float(row['open'])) :
        return 'NaN'
    else:
        return float(row['pm_volume'])*float(row['open'])

df['pm_dollar_volume'] = df.apply(pm_dolls, axis=1) # à supprimer au prochain run du data_retriever


# Save the modified DataFrame back to the CSV file
df.to_csv(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\full.csv', index=False)
