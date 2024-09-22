#coding: utf-8
#source activate py38

import metrics

"""
- il faudra faire une boucle pour le niveau de confiance (0.5, 0.6, 0.7, ...)
- return (ok)
- CAGR (ok)
- average trade (ok)
- win rate (ok)
- max drawdown (ok)
- Sharpe (ok)
- Sortino Ratio
- Profit Factor
- best trade
- worst trade

"""

def calculate_results(name, description, filters, model_name, model_type, df, random_test_set, period_duration):
    print('Calculating results for ', name)
    occurences = df.shape[0] # nb de trades
    df['cumulative_returns'] = df['returns'].cumprod()
    df['cumulative_returns'] = df['cumulative_returns'] -1
    compounded_return = df['returns'].prod()
    #cagr = metrics.calculate_cagr(df)
    cagr = 0
    average_trade = df['returns'].mean()-1
    win_rate = metrics.win_rate(df)
    max_drawdown = metrics.max_drawdown(df)
    max_consecutives_losses = metrics.max_consecutives_losses(df)
    #sharpe_ratio = metrics.sharpe(df, cagr)
    sharpe_ratio = 0
    #sortino_ratio = metrics.calculate_sortino_ratio(df['returns'], cagr)
    sortino_ratio = 0

    print('# of trades : ', occurences)
    print('compounded_return : ',compounded_return)
    print('cagr : ',cagr)
    print('average_trade : ',average_trade)
    print('win_rate : ',win_rate)
    print('max_drawdown : ',max_drawdown)
    print('max_consecutives_losses : ',max_consecutives_losses)
    print('sharpe_ratio : ',sharpe_ratio)
    print('sortino_ratio : ',sortino_ratio)

    start_date = df['date'].min()
    end_date = df['date'].max()

    # name,description,filters,model_name,model_type,occurences,compounded_return,cagr,average_trade,win_rate,max_drawdown,max_consecutives_losses,sharpe_ratio,sortino_ratio,start_date,end_date
    new_line = str(name) + ','+str(description) + ','+str(filters) + ','+str(model_name) + ','+str(model_type) + ','+str(occurences) + ','+str(compounded_return) + ','+str(cagr) + ','+str(average_trade) + ','+str(win_rate) + ','+str(max_drawdown) + ','+str(max_consecutives_losses) + ','+str(sharpe_ratio) + ','+str(sortino_ratio)+ ','+str(start_date)+ ','+str(end_date) +','+str(random_test_set) +','+str(period_duration) + '\n'
    fd = open("./data/results.csv",'a')
    fd.write(str(new_line))
    fd.close()

    df.to_csv('./data/trades/final_df_'+name+'.csv', index=True)
