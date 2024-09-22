#coding: utf-8
#source activate py38


"""
first line CSV
ticker,date,week_day,open,high,close,low,freeFloat,floatShares,market_cap,outstandingShares,volume,dollar_volume,average_volume,average_volume_previous_day,average_dollar_volume_previous_day,relative_volume,float_rotation,pm_float_rotation,pm_volume,average_dollar_volume_per_transaction,gap,x_day_high_at_open,x_day_low_at_open,previous_day_close,sigma,sigma_at_open,sigma_previous_day,sigma_change_at_open,sigma_percent_at_open,max_up,max_down,open_from_20sma,open_from_50sma,open_from_200sma,sigma_ratio_open_from_20sma,consecutive_days_above_20sma,open_from_BB_up,open_from_BB_down,1month_rolling_max,1month_change_from_high,1month_change_from_high_at_open,3month_change_from_high,6month_change_from_high,red_days,green_days,pm_dollar_volume,first_15min_move,first_15min_max_up,first_15min_max_down,first_15min_volume,first_15_min_relative_volume,first_hour_move,first_hour_max_up,first_hour_max_down,first_hour_volume,first_hour_relative_volume,open_to_close_move,open_to_close_max_up,open_to_close_max_down,open_to_close_volume,open_to_close_relative_volume,power_hour_move,power_hour_max_up,power_hour_max_down,power_hour_volume,power_hour_relative_volume,first_hour_to_close_move,first_hour_to_close_max_up,first_hour_to_close_max_down,first_hour_to_close_volume,first_hour_to_close_relative_volume,first_hour_to_power_hour_move,first_hour_to_power_hour_max_up,first_hour_to_power_hour_max_down,first_hour_to_power_hour_volume,first_hour_to_power_hour_relative_volume,open_to_power_hour_move,open_to_power_hour_max_up,open_to_power_hour_max_down,open_to_power_hour_volume,open_to_power_hour_relative_volume,duration_before_breakout_of_pm_high,move_from_breakout_of_pm_high,lower_move_before_breakout_of_pm_high,duration_below_open,duration_below_9ema,duration_below_9ema_first_hour,duration_below_20ema,duration_below_20ema_first_hour,duration_below_vwap,duration_below_vwap_first_hour,number_of_red_candles_one_hour_before_open,percent_of_red_candles_one_hour_before_open,number_of_red_candles_one_hour_after_open,percent_of_red_candles_one_hour_after_open,number_of_red_candles_during_open,percent_of_red_candles_during_open,from_pm_high_to_open,pm_high_vs_high,pm_retracement,break_200sma,test_of_pm_high,days_til_next_earnings,eps_diff_percent,revenue_diff_percent
"""

big_cap_surge = ['AAPL','TSLA','BABA','AMZN','META','TSCO','SHOP','SBUX','MSFT','PYPL','PTON','NVDA','AMD','GOOGL','PLTR','SPY','QQQ','MRNA','JPM','CSCO','ZM','ZIM','XPEV','XOM','XEL','X','WPP','WOW','WOR','WMT','WFC','WES','WDAY','WBA','VZ','VVR','VRTX','VRSN','VRSK','VOD','VOC','VEU','VEA','V','USB','UPS','UNH','TXN','TW','TSN','TSM','TMUS','TMO','TME','TM','TLS','TEAM','TCOM','T','SWKS','SUN','SQ','SPOT','SPLK','SNPS','SMIN','SIRI','SIG','SAR','SAP','RSG','ROST','ROKU','RMD','RKT','RIO','RFG','REGN','QCOM','PSN','PSI','PRU','PPT','PPH','PNI','PM','PHM','PG','PFE','PEP','PEN','PDN','PDD','PCAR','PBH','PAYX','OSH','ORI','ORCL','ORA','OKTA','NXPI','NWS','NWL','NWG','NVX','NVT','NVS','NVO','NTES','NKE','NIC','NHC','NG','NFLX','NEE','NEA','NAN','MYO','MU','MTX','MTCH','MSB','MRVL','MRO','MNST','MMS','MMM','MIN','MGR','MFG','MELI','MDT','MDLZ','MCY','MCHP','MCD','MAR','MA','M','LUV','LULU','LTHM','LSF','LRCX','LOV','LIN','LFG','LAND','KO','KLAC','KHC','JNJ','JHX','JHG','JD','ISRG','IOO','INTU','ING','INCY','ILMN','III','IHG','IFN','IDXX','IAG','HOOD','HON','HMC','HL','HEI','HD','GTY','GSK','GS','GPS','GNE','GM','GILD','GEM','GE','FPH','FOX','FLTR','FLT','FISV','FERG','FDX','FCX','FAST','F','EXC','EVT','EVR','EVN','ENR','EMN','EML','ELD','EDV','EBAY','EA','DXCM','DTE','DOW','DOCU','DLX','DLTR','DIS','DHR','CYB','CVX','CTSH','CTAS','CSX','CSR','CSL','CRWD','CRM','CRH','CPRT','CPG','COST','COE','CMCSA','CLW','CIM','CIA','CHTR','CHN','CHKP','CGC','CEN','CDW','CDNS','CCL','BVS','BTA','BSL','BPT','BP','BOE','BMY','BME','BLND','BLD','BKNG','BIIB','BIDU','BHP','BEN','BBY','BAP','BAL','BAC','BA','AZN','AVGO','AUB','ATVI','ASX','ASML','ASM','ASB','ARB','AR','APT','APO','API','APE','APA','ANSS','AMP','AMGN','AMC','AMAT','ALX','ALV','ALL','ALGN','AIZ','AIA','AHT','AHG','AGL','AGG','AEP','AEF','ADT','ADSK','ADM','ADI','ADBE','ABT','ABBV','AAL','AAA','1ADS']

clean_list = ['BABA','AMZN','META','TSLA','TSCO','SHOP','SBUX','MSFT','PYPL','PTON','NVDA','AMD','GOOGL','PLTR','SPY','QQQ','MRNA','JPM','CSCO','AAPL','ZM','ZIM','XPEV','XOM','XEL','X','WPP','WOW','WOR','WMT','WFC','WES','WDAY','WBA','VZ','VVR','VRTX','VRSN','VRSK','VOD','VOC','VEU','VEA','V','USB','UPS','UNH','TXN','TW','TSN','TSM','TMUS','TMO','TME','TM','TLS','TEAM','TCOM','T','SWKS','SUN','SQ','SPOT','SPLK','SNPS','SMIN','SIRI','SIG','SAR','SAP','RSG','ROST','ROKU','RMD','RKT','RIO','RFG','REGN','QCOM','PSN','PSI','PRU','PPT','PPH','PNI','PM','PHM','PG','PFE','PEP','PEN','PDN','PDD','PCAR','PBH','PAYX','OSH','ORI','ORCL','ORA','OKTA','NXPI','NWS','NWL','NWG','NVX','NVT','NVS','NVO','NTES','NKE','NIC','NHC','NG','NFLX','NEE','NEA','NAN','MYO','MU','MTX','MTCH','MSB','MRVL','MRO','MNST','MMS','MMM','MIN','MGR','MFG','MELI','MDT','MDLZ','MCY','MCHP','MCD','MAR','MA','M','LUV','LULU','LTHM','LSF','LRCX','LOV','LIN','LFG','LAND','KO','KLAC','KHC','JNJ','JHX','JHG','JD','ISRG','IOO','INTU','ING','INCY','ILMN','III','IHG','IFN','IDXX','IAG','HOOD','HON','HMC','HL','HEI','HD','GTY','GSK','GS','GPS','GNE','GM','GILD','GEM','GE','FPH','FOX','FLTR','FLT','FISV','FERG','FDX','FCX','FAST','F','EXC','EVT','EVR','EVN','ENR','EMN','ELD','EDV','EBAY','EA','DXCM','DTE','DOW','DOCU','DLX','DLTR','DIS','DHR','CYB','CVX','CTSH','CTAS','CSX','CSR','CSL','CRWD','CRM','CRH','CPRT','CPG','COST','COE','CMCSA','CLW','CIM','CIA','CHTR','CHN','CHKP','CGC','CEN','CDW','CDNS','CCL','BVS','BTA','BSL','BPT','BP','BOE','BMY','BME','BLND','BLD','BKNG','BIIB','BIDU','BHP','BEN','BBY','BAP','BAL','BAC','BA','AZN','AVGO','AUB','ATVI','ASX','ASML','ASM','ASB','ARB','AR','APT','APO','API','APE','APA','ANSS','AMP','AMGN','AMC','AMAT','ALX','ALV','ALL','ALGN','AIZ','AIA','AHT','AHG','AGL','AGG','AEP','AEF','ADT','ADSK','ADM','ADI','ADBE','ABT','ABBV','AAL','AAA','1ADS']

tickers = ['TEAM','TCOM','T','SWKS','SUN','SQ','SPOT','SPLK','SNPS','SMIN','SIRI','SIG','SAR','SAP','RSG','ROST','ROKU','RMD','RKT','RIO','RFG','REGN','QCOM','PSN','PSI','PRU','PPT','PPH','PNI','PM','PHM','PG','PFE','PEP','PEN','PDN','PDD','PCAR','PBH','PAYX','OSH','ORI','ORCL','ORA','OKTA','NXPI','NWS','NWL','NWG','NVX','NVT','NVS','NVO','NTES','NKE','NIC','NHC','NG','NFLX','NEE','NEA','NAN','MYO','MU','MTX','MTCH','MSB','MRVL','MRO','MNST','MMS','MMM','MIN','MGR','MFG','MELI','MDT','MDLZ','MCY','MCHP','MCD','MAR','MA','M','LUV','LULU','LTHM','LSF','LRCX','LOV','LIN','LFG','LAND','KO','KLAC','KHC','JNJ','JHX','JHG','JD','ISRG','IOO','INTU','ING','INCY','ILMN','III','IHG','IFN','IDXX','IAG','HOOD','HON','HMC','HL','HEI','HD','GTY','GSK','GS','GPS','GNE','GM','GILD','GEM','GE','FPH','FOX','FLTR','FLT','FISV','FERG','FDX','FCX','FAST','F','EXC','EVT','EVR','EVN','ENR','EMN','ELD','EDV','EBAY','EA','DXCM','DTE','DOW','DOCU','DLX','DLTR','DIS','DHR','CYB','CVX','CTSH','CTAS','CSX','CSR','CSL','CRWD','CRM','CRH','CPRT','CPG','COST','COE','CMCSA','CLW','CIM','CIA','CHTR','CHN','CHKP','CGC','CEN','CDW','CDNS','CCL','BVS','BTA','BSL','BPT','BP','BOE','BMY','BME','BLND','BLD','BKNG','BIIB','BIDU','BHP','BEN','BBY','BAP','BAL','BAC','BA','AZN','AVGO','AUB','ATVI','ASX','ASML','ASM','ASB','ARB','AR','APT','APO','API','APE','APA','ANSS','AMP','AMGN','AMC','AMAT','ALX','ALV','ALL','ALGN','AIZ','AIA','AHT','AHG','AGL','AGG','AEP','AEF','ADT','ADSK','ADM','ADI','ADBE','ABT','ABBV','AAL','AAA','1ADS']

tickers_sans_issue = ['AAPL', 'TSLA', 'BABA', 'AMZN', 'META', 'TSCO', 'SHOP', 'SBUX', 'MSFT', 'PYPL', 'PTON', 'NVDA', 'AMD', 'GOOGL', 'PLTR', 'SPY', 'QQQ', 'MRNA', 'JPM', 'CSCO', 'ZM', 'ZIM', 'XPEV', 'XOM', 'XEL', 'X', 'WPP', 'WOW', 'WOR', 'WMT', 'WFC', 'WES', 'WDAY', 'WBA', 'VZ', 'VRTX', 'VRSN', 'VRSK', 'VOD', 'VEU', 'V', 'USB', 'UPS', 'UNH', 'TXN', 'TW', 'TSN', 'TSM', 'TMUS', 'TMO', 'TME', 'TM', 'TEAM', 'TCOM', 'T', 'SWKS', 'SUN', 'SQ', 'SPOT', 'SPLK', 'SNPS', 'SIRI', 'SIG', 'SAP', 'RSG', 'ROST', 'ROKU', 'RMD', 'RKT', 'RIO', 'REGN', 'QCOM', 'PSN', 'PRU', 'PM', 'PHM', 'PG', 'PFE', 'PEP', 'PEN', 'PDD', 'PCAR', 'PBH', 'PAYX', 'ORI', 'ORCL', 'ORA', 'OKTA', 'NXPI', 'NWS', 'NWL', 'NWG', 'NVT', 'NVS', 'NVO', 'NTES', 'NKE', 'NIC', 'NG', 'NFLX', 'NEE', 'NEA', 'MU', 'MTX', 'MTCH', 'MRVL', 'MRO', 'MNST', 'MMS', 'MMM', 'MFG', 'MELI', 'MDT', 'MDLZ', 'MCY', 'MCHP', 'MCD', 'MAR', 'MA', 'M', 'LUV', 'LULU', 'LTHM', 'LRCX', 'LIN', 'KO', 'KLAC', 'KHC', 'JNJ', 'JHX', 'JHG', 'JD', 'ISRG', 'IOO', 'INTU', 'ING', 'INCY', 'ILMN', 'IHG', 'IDXX', 'IAG', 'HOOD', 'HON', 'HMC', 'HL', 'HEI', 'HD', 'GTY', 'GSK', 'GS', 'GPS', 'GM', 'GILD', 'GE', 'FOX', 'FLT', 'FERG', 'FDX', 'FCX', 'FAST', 'F', 'EXC', 'EVT', 'EVR', 'ENR', 'EMN', 'EBAY', 'EA', 'DXCM', 'DTE', 'DOW', 'DOCU', 'DLTR', 'DIS', 'DHR', 'CVX', 'CTSH', 'CTAS', 'CSX', 'CSR', 'CSL', 'CRWD', 'CRM', 'CRH', 'CPRT', 'CPG', 'COST', 'CMCSA', 'CIM', 'CHTR', 'CHKP', 'CDW', 'CDNS', 'CCL', 'BP', 'BMY', 'BLD', 'BKNG', 'BIIB', 'BIDU', 'BHP', 'BEN', 'BBY', 'BAP', 'BAC', 'BA', 'AZN', 'AVGO', 'AUB', 'ATVI', 'ASX', 'ASML', 'ASB', 'AR', 'APO', 'APE', 'APA', 'ANSS', 'AMP', 'AMGN', 'AMC', 'AMAT', 'ALV', 'ALL', 'ALGN', 'AIZ', 'AGL', 'AGG', 'AEP', 'ADT', 'ADSK', 'ADM', 'ADI', 'ADBE', 'ABT', 'ABBV', 'AAL']

# tickers surge trader ayant eu le plus de volume en dollar en juillet 23
top100_volume = ['AAPL','AMZN','GOOGL','MSFT','TSLA','NVDA','UNH','XPEV','JPM','TSM','TXN','TMUS','NFLX','AVGO','ATVI','ADBE','BAC','DIS','JNJ','CRM','PEP','COST','ASML','BA','ORCL','CVX','QCOM','MU','PG','T','HD','MA','GS','AMAT','CCL','BKNG','NKE','ISRG','F','KO','INTU','PFE','CMCSA','LRCX','ABBV','MELI','DHR','PDD','SQ','MRVL','AMGN','ADI','MCD','HON','NEE','ROKU','ABT','MDLZ','LIN','CRWD','NXPI','AZN','BMY','FDX','REGN','KLAC','FCX','CHTR','GM','GE','CSX','GILD','PM','MCHP','SNPS','AAL','CDNS','LULU','JD','MDT','MAR','BIIB','ADSK','DXCM','MMM','EA','TEAM','PAYX','MRO','IDXX','ILMN','KHC','CTAS','MNST','AEP','SPOT','BP','DLTR','ALGN','LUV','PCAR','EBAY','EXC','BIDU','ROST','FAST','ALL','DOW','CTSH']

top100_volume2 = ['ATVI','ADBE','BAC','DIS','JNJ','CRM','PEP','COST','ASML','BA','ORCL','CVX','QCOM','MU','PG','T','HD','MA','GS','AMAT','CCL','BKNG','NKE','ISRG','F','KO','INTU','PFE','CMCSA','LRCX','ABBV','MELI','DHR','PDD','SQ','MRVL','AMGN','ADI','MCD','HON','NEE','ROKU','ABT','MDLZ','LIN','CRWD','NXPI','AZN','BMY','FDX','REGN','KLAC','FCX','CHTR','GM','GE','CSX','GILD','PM','MCHP','SNPS','AAL','CDNS','LULU','JD','MDT','MAR','BIIB','ADSK','DXCM','MMM','EA','TEAM','PAYX','MRO','IDXX','ILMN','KHC','CTAS','MNST','AEP','SPOT','BP','DLTR','ALGN','LUV','PCAR','EBAY','EXC','BIDU','ROST','FAST','ALL','DOW','CTSH']

#
# 100B & 10M de V
#tickers = ['RY','HD','UL','AVGO','ORCL','NEE','RTX','T','BX','HSBC','WFC','UNP','HDB','JPM','GS','MA','COST','TSM','TXN','SAP','PFE','HON','LOW',,'ASML','V','TMO','DIS','MS','GOOG','INTC','BLK','GOOGL','ACN','BAC','DHR','SPGI','AMZN','AMD','BABA','NKE','INTU','CRM','TSLA','NFLX','NVDA','ADBE']
# faire FB et META à part + 'BRK.A'

import time
import fin_functions
#from polygon import RESTClient
import pandas
import numpy as np
from analysis import low_tf
from datetime import date, timedelta
import os

i = 0

start_date = date(2023, 8, 1)
end_date = date(2023, 11, 26)
path = "./historical_data/top100_clean.csv"

def main():
    print('Starting...')
    master_loop()

    """
    try :
        master_loop()
    except Exception as e: print('error: ' , e)
    """


def master_loop():
    # master loop for each ticker
    for t in top100_volume2:
        print(t)
        #try :

        # retrieve daily data
        df_daily = fin_functions.get_daily_data(t, start_date, end_date)
        df_daily = fin_functions.get_days_til_earnings(t, end_date, df_daily)


        if isinstance(df_daily, pandas.DataFrame) :
            new_daily_df = daily_loop(t, df_daily) # daily analysis

            if type(new_daily_df) != bool :
                intraday_loop(t, new_daily_df)

        #except Exception as e: print('error: ' , e)


# master loop for each ticker : ajoute des données au dataframe daily (float, sma, gap etc)
def daily_loop(t, df_daily):
    # base
    df_daily['ticker'] = t

    # global data (tout ce qui ne change pas d'un jour sur l'autre)
    float_data = fin_functions.get_float(t)

    if len(float_data) == 0:
        print('données pmp indisponibles')
        return False
    else:
        # company size and shares
        df_daily['freeFloat'] = float_data[0]['freeFloat']
        df_daily['floatShares'] = float_data[0]['floatShares']
        df_daily['outstandingShares'] = float_data[0]['outstandingShares']
        df_daily['market_cap'] = df_daily['o'] * float_data[0]['outstandingShares']


        # volume
        df_daily['dollar_volume'] = df_daily['v']*df_daily['c']
        df_daily['average_volume'] = df_daily['v'].rolling(window=10).mean()
        df_daily['average_volume_previous_day'] = df_daily['average_volume'].shift(1)
        df_daily['average_dollar_volume_previous_day'] = df_daily['average_volume'].shift(1)*df_daily['c'].shift(1)
        df_daily['relative_volume'] = df_daily['v']/df_daily['average_volume']
        df_daily['float_rotation'] = df_daily['v']/df_daily['floatShares']
        df_daily['average_dollar_volume_per_transaction'] = df_daily['v']*df_daily['c']/df_daily['n']


        # move
        df_daily['gap'] = (df_daily['o'] - df_daily['c'].shift(1)) / df_daily['c'].shift(1)
        df_daily['previous_day_close'] = df_daily['c'].shift(1)

        # Appliquez la fonction custom_rolling à chaque fenêtre de 20 jours
        def rolling_std_with_open(window):
            window[-1] = df_daily['o'].iloc[window.index[-1]]
            return np.std(window)

        def rolling_mean_with_open(window):
            window[-1] = df_daily['o'].iloc[window.index[-1]]
            return np.mean(window)



        df_daily['sigma'] = df_daily['c'].rolling(20).std() # ne peut être utiliser pour prédire intraday move
        df_daily['sigma_at_open'] = df_daily['c'].shift(1).rolling(window=19).apply(rolling_std_with_open, raw=False)
        df_daily['sigma_previous_day'] = df_daily['c'].rolling(20).std().shift(1)
        df_daily['sigma_change_at_open'] = df_daily['sigma_at_open'] / df_daily['sigma_previous_day'] -1
        df_daily['sigma_percent_at_open'] = df_daily['sigma_at_open'] / df_daily['c']
        df_daily['max_up'] = (df_daily['h'] - df_daily['o']) / df_daily['o']
        df_daily['max_down'] = (df_daily['l'] - df_daily['o']) / df_daily['o']


        # daily indicators
        df_daily['20sma'] = df_daily['c'].rolling(20).mean()
        df_daily['20sma_at_open'] = df_daily['c'].shift(1).rolling(window=19).apply(rolling_mean_with_open, raw=False) # utilise l'open pour la dernière valeur
        df_daily['50sma'] = df_daily['c'].rolling(50).mean()
        df_daily['50sma_at_open'] = df_daily['c'].shift(1).rolling(window=49).apply(rolling_mean_with_open, raw=False) # utilise l'open pour la dernière valeur
        df_daily['200sma'] = df_daily['c'].rolling(200).mean()
        df_daily['200sma_at_open'] = df_daily['c'].shift(1).rolling(window=199).apply(rolling_mean_with_open, raw=False)

        df_daily['BB_up'] = df_daily['20sma'] + 2 * df_daily['sigma']
        df_daily['BB_up_at_open'] = df_daily['20sma_at_open'] + 2 * df_daily['sigma_at_open']
        df_daily['BB_down'] = df_daily['20sma'] - 2 * df_daily['sigma']
        df_daily['BB_down_at_open'] = df_daily['20sma_at_open'] - 2 * df_daily['sigma_at_open']

        #df_daily['above_20sma'] = df_daily['c'] > df_daily['20sma']
        #df_daily['above_50sma'] = df_daily['c'] > df_daily['50sma']
        #df_daily['above_200sma'] = df_daily['c'] > df_daily['200sma']

        df_daily['open_from_20sma'] = (df_daily['20sma_at_open'] - df_daily['o']) / df_daily['o']
        df_daily['open_from_50sma'] = (df_daily['50sma_at_open'] - df_daily['o']) / df_daily['o']
        df_daily['open_from_200sma'] = (df_daily['200sma_at_open'] - df_daily['o']) / df_daily['o']

        df_daily['sigma_ratio_open_from_20sma'] = ((df_daily['20sma_at_open'] - df_daily['o']) / df_daily['o'])/df_daily['sigma_percent_at_open']

        df_daily['open_from_BB_up'] = (df_daily['BB_up_at_open'] - df_daily['o']) / df_daily['o']
        df_daily['open_from_BB_down'] = (df_daily['BB_down_at_open'] - df_daily['o']) / df_daily['o']

        #df_daily['date'] = df_daily['t']
        #df_daily['date'] = pandas.to_datetime(df_daily['date'])
        df_daily.set_index('date', inplace=True)
        df_daily['1month_rolling_max'] = df_daily['h'].rolling(window='30D').max()
        df_daily['1month_change_from_high'] = ((df_daily['c'] - df_daily['1month_rolling_max']) / df_daily['1month_rolling_max']).shift(1)
        df_daily['1month_change_from_high_at_open'] = ((df_daily['o'] - df_daily['1month_rolling_max'].shift(1)) / df_daily['1month_rolling_max'].shift(1))
        df_daily['3month_rolling_max'] = df_daily['h'].rolling(window='90D').max()
        df_daily['3month_change_from_high'] = ((df_daily['c'] - df_daily['3month_rolling_max']) / df_daily['3month_rolling_max']).shift(1)
        df_daily['6month_rolling_max'] = df_daily['h'].rolling(window='180D').max()
        df_daily['6month_change_from_high'] = ((df_daily['c'] - df_daily['6month_rolling_max']) / df_daily['6month_rolling_max']).shift(1)

        df_daily = df_daily.reset_index(drop=True)


        # red_days & green_days & consecutive_days_above_20sma
        for i in range(0, len(df_daily)):
            # red_days
            if i == 0 or i==1:
                df_daily.loc[i, 'red_days'] = 0
            elif df_daily.loc[i-1, 'c'] < df_daily.loc[i-2, 'c']:
                df_daily.loc[i, 'red_days'] = df_daily.loc[i-1, 'red_days'] + 1
            else:
                df_daily.loc[i, 'red_days'] = 0

            # green_days
            if i == 0 or i==1:
                df_daily.loc[i, 'green_days'] = 0
            elif df_daily.loc[i-1, 'c'] > df_daily.loc[i-2, 'c']:
                df_daily.loc[i, 'green_days'] = df_daily.loc[i-1, 'green_days'] + 1
            else:
                df_daily.loc[i, 'green_days'] = 0

            # consecutive_days_above_20sma (à j-1)
            if i == 0:
                df_daily.loc[i, 'consecutive_days_above_20sma'] = 0
            elif df_daily.loc[i-1, '20sma'] < df_daily.loc[i-1, 'c']:
                df_daily.loc[i, 'consecutive_days_above_20sma'] = df_daily.loc[i-1, 'consecutive_days_above_20sma'] + 1
            else:
                df_daily.loc[i, 'consecutive_days_above_20sma'] = 0

        # lundi, mardi, mercredi ...
        df_daily['week_day'] = pandas.to_datetime(df_daily['t']).dt.day_name()

        # "ouvre sur un plus haut de [x_day_high_at_open] jours"
        df_daily['x_day_high_at_open'] = 0
        for n in reversed(range(len(df_daily['h']))):
            for i in reversed(range(n)):
                if df_daily['o'][n] > df_daily['h'][i]:
                    df_daily['x_day_high_at_open'][n] = n - i
                else: break

        # "ouvre sur un plus bas de [x_day_high_at_open] jours"
        df_daily['x_day_low_at_open'] = 0
        for n in reversed(range(len(df_daily['l']))):
            for i in reversed(range(n)):
                if df_daily['o'][n] < df_daily['l'][i]:
                    df_daily['x_day_low_at_open'][n] = n - i
                else: break


        #output_file_name = f"./historical_data/consolidated_data_06082023.csv"
        #df_daily.to_csv(output_file_name, index=False)
        formated_start_date = pandas.to_datetime(start_date)
        df_daily = df_daily[df_daily['t'] >= formated_start_date]
        return df_daily



def intraday_loop(t, new_daily_df):
    for index, row in new_daily_df.iterrows():
        print(str(row['t'])[:10])
        #try :
        pm_volume, first_15min_move, first_15min_max_up, first_15min_max_down, first_15min_volume, first_15_min_relative_volume, first_hour_move, first_hour_max_up, first_hour_max_down, first_hour_volume, first_hour_relative_volume, open_to_close_move, open_to_close_max_up, open_to_close_max_down, open_to_close_volume, open_to_close_relative_volume, power_hour_move, power_hour_max_up, power_hour_max_down, power_hour_volume, power_hour_relative_volume, first_hour_to_close_move, first_hour_to_close_max_up, first_hour_to_close_max_down, first_hour_to_close_volume, first_hour_to_close_relative_volume, first_hour_to_power_hour_move, first_hour_to_power_hour_max_up, first_hour_to_power_hour_max_down, first_hour_to_power_hour_volume, first_hour_to_power_hour_relative_volume, open_to_power_hour_move, open_to_power_hour_max_up, open_to_power_hour_max_down, open_to_power_hour_volume, open_to_power_hour_relative_volume, duration_before_breakout_of_pm_high, move_from_breakout_of_pm_high, lower_move_before_breakout_of_pm_high, duration_below_open, duration_below_9ema, duration_below_9ema_first_hour, duration_below_20ema, duration_below_20ema_first_hour, duration_below_vwap, duration_below_vwap_first_hour, number_of_red_candles_one_hour_before_open, percent_of_red_candles_one_hour_before_open, number_of_red_candles_one_hour_after_open, percent_of_red_candles_one_hour_after_open, number_of_red_candles_during_open, percent_of_red_candles_during_open, from_pm_high_to_open, pm_high_vs_high, pm_retracement, break_200sma, test_of_pm_high = low_tf(str(row['t'])[:10], t, row['average_volume'], row['gap'], row['previous_day_close'], row['200sma'] )

        if pm_volume != 'na' and row['floatShares'] != 0 :
            pm_float_rotation = pm_volume / row['floatShares']
        else :
            pm_float_rotation = 'na'

        if pm_volume != 'na' :
            pm_dollar_volume = pm_volume * row['o']
        else :
            pm_dollar_volume = 'na'


        new_line = str(t) + ',' + str(row['t'])[:10] + ',' + str(row['week_day']) + ',' + str(row['o']) + ',' + str(row['h']) + ',' + str(row['c']) + ',' + str(row['l']) + ',' + str(row['freeFloat']) + ',' + str(row['floatShares']) + ','+ str(row['market_cap']) + ','+str(row['outstandingShares']) + ','+str(row['v']) + ',' + str(row['dollar_volume']) + ','+str(row['average_volume']) + ',' +str(row['average_volume_previous_day']) + ','+str(row['average_dollar_volume_previous_day']) + ','+str(row['relative_volume']) + ','+str(row['float_rotation']) + ','  +str(pm_float_rotation) +','+ str(pm_volume) + ','+str(row['average_dollar_volume_per_transaction']) + ','+str(row['gap']) + ','+str(row['x_day_high_at_open']) + ','+str(row['x_day_low_at_open']) + ','+str(row['previous_day_close']) + ','+str(row['sigma']) + ',' + str(row['sigma_at_open']) + ','+str(row['sigma_previous_day']) + ','+ str(row['sigma_change_at_open']) +','+ str(row['sigma_percent_at_open']) + ','+str(row['max_up']) + ','+str(row['max_down']) + ','+str(row['open_from_20sma']) + ','+str(row['open_from_50sma']) + ','+str(row['open_from_200sma']) + ','+str(row['sigma_ratio_open_from_20sma']) + ',' +str(row['consecutive_days_above_20sma']) + ',' +str(row['open_from_BB_up']) + ','+str(row['open_from_BB_down']) + ','+str(row['1month_rolling_max']) +','+str(row['1month_change_from_high']) +','+str(row['1month_change_from_high_at_open']) +','+str(row['3month_change_from_high'])  + ','+str(row['6month_change_from_high']) + ','+str(row['red_days']) +  ','+str(row['green_days']) + ',' + str(pm_dollar_volume) + ','+str( first_15min_move) + ','+str( first_15min_max_up) + ','+str( first_15min_max_down) + ','+str( first_15min_volume) + ','+str( first_15_min_relative_volume) + ','+str( first_hour_move) + ','+str( first_hour_max_up) + ','+str( first_hour_max_down) + ','+str( first_hour_volume) + ','+str( first_hour_relative_volume) + ','+str( open_to_close_move) + ','+str( open_to_close_max_up) + ','+str( open_to_close_max_down) + ','+str( open_to_close_volume) + ','+str( open_to_close_relative_volume) + ','+str( power_hour_move) + ','+str( power_hour_max_up) + ','+str( power_hour_max_down) + ','+str( power_hour_volume) + ','+str( power_hour_relative_volume) + ','+str( first_hour_to_close_move) + ','+str( first_hour_to_close_max_up) + ','+str( first_hour_to_close_max_down) + ','+str( first_hour_to_close_volume) + ','+str( first_hour_to_close_relative_volume) + ','+str( first_hour_to_power_hour_move) + ','+str( first_hour_to_power_hour_max_up) + ','+str( first_hour_to_power_hour_max_down) + ','+str( first_hour_to_power_hour_volume) + ','+str( first_hour_to_power_hour_relative_volume) + ','+str( open_to_power_hour_move) + ','+str( open_to_power_hour_max_up) + ','+str( open_to_power_hour_max_down) + ','+str( open_to_power_hour_volume) + ','+str( open_to_power_hour_relative_volume) + ','+str( duration_before_breakout_of_pm_high) + ',' +str( move_from_breakout_of_pm_high) + ',' +str( lower_move_before_breakout_of_pm_high) + ','+str( duration_below_open) + ','+str( duration_below_9ema) + ','+str( duration_below_9ema_first_hour) + ','+str( duration_below_20ema) + ','+str( duration_below_20ema_first_hour) + ','+str( duration_below_vwap) + ','+str( duration_below_vwap_first_hour) + ','+str( number_of_red_candles_one_hour_before_open) + ','+str( percent_of_red_candles_one_hour_before_open) + ','+str( number_of_red_candles_one_hour_after_open) + ','+str( percent_of_red_candles_one_hour_after_open) + ','+str( number_of_red_candles_during_open) + ','+str( percent_of_red_candles_during_open) + ','+str( from_pm_high_to_open) + ','+str( pm_high_vs_high) + ','+str( pm_retracement) + ','+str( break_200sma) + ',' +str( test_of_pm_high) + ',' +str(row['days_til_next_earnings']) + ',' +str( row['eps_diff_percent']) + ',' +str( row['revenue_diff_percent'])+ '\n'

        fd = open(path,'a')
        fd.write(str(new_line))
        fd.close()

        #except Exception as e: print('error: ' , e)
        time.sleep(0.03)





main()







#
