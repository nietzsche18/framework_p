


import pandas as pd

# create sample data
data = {'Value': [2, 3, 5, 2, 4, 6, 6, 5]}
df = pd.DataFrame(data)

# initialize the new series with NaN values
df['red_days'] = pd.Series([float('NaN')] * len(df))

# loop through the 'Value' column and update the 'Bigger_than_previous' column
for i in range(0, len(df)):
    if i == 0:
        df.loc[i, 'red_days'] = 0
    elif df.loc[i, 'Value'] > df.loc[i-1, 'Value']:
        df.loc[i, 'red_days'] = df.loc[i-1, 'red_days'] + 1
    else:
        df.loc[i, 'red_days'] = 0

print(df)










def show_df(df):
    df_to_show = df
    df_to_show['Date'] = pandas.to_datetime(df_to_show['t'])
    df_to_show.set_index('Date', inplace=True)
    df_to_show = df_to_show[['o','h','l','c']]
    df_to_show.rename(columns={"o": "Open", "h": "High", "l":"Low", "c":"Close"}, inplace=True)
    print(df_to_show)
    mpl.plot(
        df_to_show,
        type="candle"
    )
