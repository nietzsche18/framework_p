import pandas as pd

import math

# Read in the CSV file as a Pandas DataFrame
df = pd.read_csv(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\full.csv')

# Calculate if column A is above column B
def compare(row):
    if math.isnan(row['200sma']):
        return 'NA'
    else:
        return row['open'] > row['200sma']

df['above_200sma'] = df.apply(compare, axis=1)
pd.set_option('display.max_columns', None)
print(df.head(40))

# Save the modified DataFrame back to the CSV file
df.to_csv(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\full.csv', index=False)
