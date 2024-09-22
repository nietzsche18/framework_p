#coding: utf-8
#source activate py38

'''
1. Extract list of strategies from StrategyInstances and loop through it
2. Check if there is a csv related
3. Loop through algos
4. Save results in csv

PrepClass prepares the data
StrategyClass describes how the strategy will function
StrategyInstances are instances of StrategyClass and constitute a list of strategies
results calculates stats related to each instance (sharpe, drawdown ... )
'''

from StrategyInstances import strategy_list

duration = 5

for strat in strategy_list:
    print(strat.description)
    #print('début', strat.prepared_data.data['date'].min())
    #print('fin', strat.prepared_data.data['date'].max())
    for algo in strat.models:
        strat.predict(algo, False, duration)









#
