import requests
import json
from datetime import date, timedelta
import pandas
import os

API_KEY_FINANCIAL = os.getenv('API_KEY_FINANCIAL')
API_KEY_POLYGON = os.getenv('API_KEY_POLYGON')

# Récupère le float (API payante)
def get_float(ticker):
    url = f"https://financialmodelingprep.com/api/v4/shares_float?symbol={ticker}&apikey={API_KEY_FINANCIAL}"
    response = requests.get(url)
    #print(json.dumps(response.json(), indent=1))
    return response.json()

#get_float("DRUG")



def get_5min_data(ticker, single_date):
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/5/minute/{single_date}/{single_date}?adjusted=true&sort=asc&apiKey={API_KEY_POLYGON}"
    response = requests.get(url)
    #print(json.dumps(response.json(), indent=1))
    return response.json()['results']

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def get_daily_data(ticker, start_date, end_date):
    for single_date in daterange(start_date, end_date):
        new_start_date = start_date - timedelta(days=90)
        url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{new_start_date.strftime('%Y-%m-%d')}/{end_date.strftime('%Y-%m-%d')}?adjusted=true&sort=asc&apiKey={API_KEY_POLYGON}"
        response = requests.get(url)
        #print(response.json())
        #print(json.dumps(response.json()['results'], indent=1))
        if 'results' in response.json():
            df = pandas.DataFrame(response.json()['results'])
            df['t'] = pandas.to_datetime(df['t'], unit='ms')
            return df
        else:
            print('ticker ', ticker , ' is not available')
            return 'na'

def get_days_til_earnings(t, end_date, df):
    url = f"https://financialmodelingprep.com/api/v3/historical/earning_calendar/{t}?apikey={API_KEY_FINANCIAL}"
    response = requests.get(url)
    earnings_df = pandas.DataFrame(response.json())
    earnings_df['date'] = pandas.to_datetime(earnings_df['date'])
    earnings_df.loc[earnings_df['time'] == 'amc', 'date'] = earnings_df.loc[earnings_df['time'] == 'amc', 'date'] + timedelta(days=2)

    df['date'] = df['t']
    df['date'] = pandas.to_datetime(df['date'].dt.date)

    df['days_til_next_earnings'] = None
    # Pour chaque ligne dans df, trouvez la prochaine date d'earnings et calculez le nombre de jours ouvrés jusqu'à cette date.
    for index, row in df.iterrows():
        next_earning_dates = earnings_df[earnings_df['date'] > row['date']]
        if not next_earning_dates.empty:
            next_date = next_earning_dates.iloc[-1]['date']
            if next_date < end_date:
                days_until_next = len(df[(df['date'] > row['date']) & (df['date'] <= next_date)])
                df.at[index, 'days_til_next_earnings'] = days_until_next
            else:
                df.at[index, 'days_til_next_earnings'] = (next_date - row['date']).days

    earnings_df['eps_diff_percent'] = ((earnings_df['eps'] - earnings_df['epsEstimated']) / earnings_df['epsEstimated']).shift(-1)
    earnings_df['revenue_diff_percent'] = ((earnings_df['revenue'] - earnings_df['revenueEstimated']) / earnings_df['revenueEstimated']).shift(-1)

    df = pandas.merge(df, earnings_df[['date', 'eps_diff_percent', 'revenue_diff_percent']], on='date', how='left')

    return df


#
