#coding: utf-8
#source activate py38

import numpy as np
from typing import List

# xgboost
import xgboost as xgb
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np

import matplotlib.pyplot as plt

import pickle

# PERSO
from PrepClass import Prepare
from results import calculate_results

class Strategy:
    def __init__(self, name: str, description: str, filters: List[str], inputs: List[str], drop_na: List[str], to_drop: List[str], models: List[str], model_type: str):
        self.name = name
        self.description = description
        self.filters = filters # e.g. market_cap > 100b
        self.inputs = inputs # columns to keep from the big dataframe with all the variables
        self.drop_na = drop_na # list of columns that must not have NA values, otherwise the column is removed
        self.to_drop = to_drop
        self.models = models
        self.model_type = model_type
        self.prepared_data = None
        self.initialize()

    def initialize(self):
        print("##################################################################")
        print("Strategy Class initialized for ", self.name)
        # Ajouter une fonction qui vérifie que full est up-to-date et update les data manquantes sinon
        df = pd.read_csv(r'C:\Users\33670\Desktop\framework\notebooks\data\top50_13082023_rolling_percentiles.csv')
        #df = pd.read_csv(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\top100_13082023.csv')
        self.prepared_data = Prepare(df, self.name,  self.filters, self.inputs, self.drop_na, self.to_drop)

    def predict(self, model_name: str, random_test_set, duration):
        # You would define your prediction function here based on the model_name chosen
        full_df = self.prepared_data.data
        full_df['date'] = pd.to_datetime(full_df['date'])
        full_df['group'] = (full_df['date'] - full_df['date'].min()) // pd.Timedelta(days=30.44 * duration)
        groups = [group.drop(columns='group') for _, group in full_df.groupby('group')]
        for data in groups:
            if model_name == 'xgboost' and self.model_type == 'classification':
                #data = pd.read_csv(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\\' + self.name +'.csv')
                X = data.drop(['date','to_predict', 'returns'], axis=1)
                y = data['to_predict']
                if random_test_set:
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=42)
                else:
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, shuffle=False)
                dtrain_reg = xgb.DMatrix(X_train, y_train, enable_categorical=True)
                dtest_reg = xgb.DMatrix(X_test, y_test, enable_categorical=True)
                params = {
                    'objective': 'binary:logistic',
                    'eval_metric': 'logloss',
                    'max_depth': 5,
                    'eta': 0.1
                }
                trained_model = xgb.train(params=params, dtrain=dtrain_reg, num_boost_round=100)
                y_pred = trained_model.predict(dtest_reg)
                X_test['pred'] = y_pred
                X_test = X_test.join(data['returns'], how='inner')
                X_test = X_test.join(data['date'], how='inner')
                X_test['date'] = pd.to_datetime(X_test['date'])
                X_test = X_test.sort_values('date')
                X_test = X_test[X_test['pred']>0.8] # détermine le niveau de confiance à partir duquel on conserve les lignes

                #calculate results
                period_duration = (data['date'].max()-data['date'].min()).days
                calculate_results(self.name, self.description, self.filters, model_name, self.model_type, X_test, random_test_set, period_duration)

                # save model
                model_path = './models/' + self.name + '.pkl'
                pickle.dump(trained_model, open(model_path, 'wb'))


                # -----------------------------------------------

                #xgb.plot_importance(trained_model)
                #plt.show()

            elif model_name == 'random_forest':
                # predict using random forest model
                pass
            else:
                # raise an error if an invalid model is chosen
                raise ValueError(f"Invalid model name: {model_name}")


            # return the predicted values
            pass





def additional_test():
    # ----- TESTING ADDITIONAL DATA -------------

    print("##################################################################")
    print('Testing data from July')
    raw_data_to_test = pd.read_csv(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\test_july23.csv')
    prepared_data_to_test = Prepare(raw_data_to_test, self.name, self.filters, self.inputs, self.drop_na, self.to_drop)
    data_to_test = prepared_data_to_test.data
    X_may = data_to_test.drop(['date','to_predict', 'returns'], axis=1)
    y_may = data_to_test['to_predict']
    dtest_reg_may = xgb.DMatrix(X_may, y_may, enable_categorical=True)
    y_pred_may = trained_model.predict(dtest_reg_may)
    X_may['pred'] = y_pred_may
    X_may = X_may.join(data_to_test['returns'], how='inner')
    X_may = X_may.join(data_to_test['date'], how='inner')
    X_may['date'] = pd.to_datetime(X_may['date'])
    X_may = X_may.sort_values('date')
    X_may = X_may[X_may['pred']>0.5] # détermine le niveau de confiance à partir duquel on conserve les lignes

    #calculate results
    calculate_results(self.name, self.description, self.filters, model_name, self.model_type, X_may)





#
