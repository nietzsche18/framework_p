#coding: utf-8
#source activate py38

"""
L'objectif est de produire un outil de backtesting qui va tester plusieurs fonctions en produit cartésien

1. Récupérer la donnée sur polygon
2. Coder les fonctions de critère d'entrée
3. Coder les fonctions de critère de sortie
4. Coder le combinateur qui enregistre les trades
5. Calculer les performances

"""

#
import json
import time

# Récupération des data sur polygon.io
import requests
#from polygon import RESTClient


'''
#print(response.json()['tickers'])
'''

# là il faut faire un bot qui va récupérer les données historiques de tous les tickers nasdaq
from datetime import date, timedelta
import os

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2022, 1, 1)
end_date = date(2022, 9, 1)

for single_date in daterange(start_date, end_date):
    print(str(single_date.strftime("%Y-%m-%d")))

    url = "https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/"+ str(single_date.strftime("%Y-%m-%d")) +"?adjusted=true&apiKey=AmUE0EZEpoHRVhOqO7OUDB6Szrugvtp0"
    response = requests.get(url)
    #print(json.dumps(response.json(), indent=1))

    if response.json()['queryCount'] != 0 :
        for el in response.json()['results']:
            try:
                #print(el['T'])
                n = 'NA'
                if 'n' in el:
                    n = el['n']
                vw = 'NA'
                if 'vw' in el:
                    vw = el['vw']

                new_line = str(single_date.strftime("%Y-%m-%d")) + ',' + str(el['c']) + ',' + str(el['h']) + ',' + str(el['l']) + ',' + str(el['o']) + ',' + str(n) + ',' + str(el['v']) + ',' + str(vw) + '\n'
                le_path = str(el['T']) +'.csv'
                if os.path.exists(le_path):
                    fd = open(le_path,'a')
                    fd.write(str(new_line))
                    fd.close()
                else:
                    #print(le_path , ' file does not exist')
                    fd = open(le_path,"a+")
                    first_line = 'date,close,high,low,open,transactions,volume,vwap\n'
                    fd.write(str(first_line))
                    fd.write(str(new_line))
                    fd.close()
            except Exception as e:
                print(str(el['T']) , 'erreur')
                print(el)
                print(e)

    time.sleep(3)















#
