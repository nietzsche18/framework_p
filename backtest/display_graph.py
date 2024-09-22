import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import requests

def get_ohlc(ticker,date):
    url = "https://api.polygon.io/v2/aggs/ticker/"+ str(ticker) +"/range/5/minute/"+ date +"/"+ date +"?adjusted=true&sort=asc&apiKey=AmUE0EZEpoHRVhOqO7OUDB6Szrugvtp0"
    response = requests.get(url)
    #print(json.dumps(response.json(), indent=1))
    return response.json()['results']

def plot_candlestick(data, title, market_open_time="13:30"):
    # Extraction de l'année, du mois et du jour pour construire la datetime de l'ouverture du marché
    year, month, day = data.index[0].year, data.index[0].month, data.index[0].day
    open_datetime = pd.to_datetime(f"{year}-{month}-{day} {market_open_time}")
    enlarged_figsize = (15,10)

    # Ajout de la délimitation verticale pour l'ouverture du marché
    fig, axes = mpf.plot(data, type='candle', style='charles', title=title, volume=True, show_nontrading=True, returnfig=True, figsize=enlarged_figsize)
    axes[0].axvline(open_datetime, color='r', linestyle='--')
    plt.show()


def main():
    # Chargement du CSV
    df = pd.read_csv(r'C:\Users\33670\Desktop\framework\notebooks\data\for_graph.csv')
    df = df.sort_values(by='open_to_close_move', ascending=False)
    df = df.dropna(subset=['open_to_close_move'])

    # Trier pour obtenir le top 20 et le bottom 20
    df['open_to_close_move'] = df['open_to_close_move'].str.replace(',', '.').astype('float')*100
    top_20 = df.sort_values(by='open_to_close_move', ascending=False).head(30)
    bottom_20 = df.sort_values(by='open_to_close_move', ascending=True).head(30)

    # Concaténer les deux dataframes
    df = pd.concat([top_20, bottom_20])


    for index, row in df.iterrows():
        date = row['date']
        ticker = row['ticker']
        open_to_close_move = row['open_to_close_move']

        ohlc_data = get_ohlc(ticker, date)
        df_5min = pd.DataFrame.from_records(ohlc_data)
        df_5min['date'] = pd.to_datetime(df_5min['t'], unit='ms')
        df_5min = df_5min.rename(columns={'o':'Open','h':'High','c':'Close','l':'Low','v':'Volume'})
        df_5min.set_index('date', inplace=True)

         # Affichage du graphique en chandeliers
        print(date, ' - ' , ticker , ' : ', open_to_close_move)
        plot_candlestick(df_5min, f"{ticker} on {date} with {open_to_close_move}")


main()
