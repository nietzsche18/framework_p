
list1 = ['AAPL', 'TSLA', 'BABA', 'AMZN', 'META', 'TSCO', 'SHOP', 'SBUX', 'MSFT', 'PYPL', 'PTON', 'NVDA', 'AMD', 'GOOGL', 'PLTR', 'SPY', 'QQQ', 'MRNA', 'JPM', 'CSCO', 'ZM', 'ZIM', 'XPEV', 'XOM', 'XEL', 'X', 'WPP', 'WOW', 'WOR', 'WMT', 'WFC', 'WES', 'WDAY', 'WBA', 'VZ', 'VRTX', 'VRSN', 'VRSK', 'VOD', 'VEU', 'V', 'USB', 'UPS', 'UNH', 'TXN', 'TW', 'TSN', 'TSM', 'TMUS', 'TMO', 'TME', 'TM', 'TEAM', 'TCOM', 'T', 'SWKS', 'SUN', 'SQ', 'SPOT', 'SPLK', 'SNPS', 'SIRI', 'SIG', 'SAP', 'RSG', 'ROST', 'ROKU', 'RMD', 'RKT', 'RIO', 'REGN', 'QCOM', 'PSN', 'PRU', 'PM', 'PHM', 'PG', 'PFE', 'PEP', 'PEN', 'PDD', 'PCAR', 'PBH', 'PAYX', 'ORI', 'ORCL', 'ORA', 'OKTA', 'NXPI', 'NWS', 'NWL', 'NWG', 'NVT', 'NVS', 'NVO', 'NTES', 'NKE', 'NIC', 'NG', 'NFLX', 'NEE', 'NEA', 'MU', 'MTX', 'MTCH', 'MRVL', 'MRO', 'MNST', 'MMS', 'MMM', 'MFG', 'MELI', 'MDT', 'MDLZ', 'MCY', 'MCHP', 'MCD', 'MAR', 'MA', 'M', 'LUV', 'LULU', 'LTHM', 'LRCX', 'LIN', 'KO', 'KLAC', 'KHC', 'JNJ', 'JHX', 'JHG', 'JD', 'ISRG', 'IOO', 'INTU', 'ING', 'INCY', 'ILMN', 'IHG', 'IDXX', 'IAG', 'HOOD', 'HON', 'HMC', 'HL', 'HEI', 'HD', 'GTY', 'GSK', 'GS', 'GPS', 'GM', 'GILD', 'GE', 'FOX', 'FLT', 'FERG', 'FDX', 'FCX', 'FAST', 'F', 'EXC', 'EVT', 'EVR', 'ENR', 'EMN', 'EBAY', 'EA', 'DXCM', 'DTE', 'DOW', 'DOCU', 'DLTR', 'DIS', 'DHR', 'CVX', 'CTSH', 'CTAS', 'CSX', 'CSR', 'CSL', 'CRWD', 'CRM', 'CRH', 'CPRT', 'CPG', 'COST', 'CMCSA', 'CIM', 'CHTR', 'CHKP', 'CDW', 'CDNS', 'CCL', 'BP', 'BMY', 'BLD', 'BKNG', 'BIIB', 'BIDU', 'BHP', 'BEN', 'BBY', 'BAP', 'BAC', 'BA', 'AZN', 'AVGO', 'AUB', 'ATVI', 'ASX', 'ASML', 'ASB', 'AR', 'APO', 'APE', 'APA', 'ANSS', 'AMP', 'AMGN', 'AMC', 'AMAT', 'ALV', 'ALL', 'ALGN', 'AIZ', 'AGL', 'AGG', 'AEP', 'ADT', 'ADSK', 'ADM', 'ADI', 'ADBE', 'ABT', 'ABBV', 'AAL']

list2 = ['TSLA','AAPL','NFLX','AVGO','ATVI','ADBE','AMZN','META','BAC','DIS','JNJ','CRM','PEP','COST','ASML','BA','ORCL','CVX','QCOM','MU','PG','T','HD','MA','GS','AMAT','CCL','BKNG','NKE','ISRG','F','KO','INTU','PFE','CMCSA','LRCX','ABBV','AGG','MELI','DHR','PDD','SQ','MRVL','AMGN','ADI','MCD','HON','NEE','ROKU','ABT','MDLZ','LIN','CRWD','NXPI','AZN','BMY','FDX','REGN','KLAC','FCX','CHTR','GM','GE','CSX','GILD','PM','MCHP','SNPS','AAL','CDNS','LULU','JD','MDT','MAR','BIIB','ADSK','DXCM','MMM','EA','TEAM','PAYX','MRO','IDXX','ILMN','KHC','CTAS','MNST','AEP','SPOT','BP','DLTR','ALGN','LUV','PCAR','EBAY','EXC','BIDU','ROST','FAST','ALL','DOW','CTSH']

def find_missing_values(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    missing_values = set1 - set2
    return list(missing_values)

# Example usage
missing_values = find_missing_values(list1, list2)

print("Missing values in list2:", missing_values)
