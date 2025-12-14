import numpy as np
from catboost import Pool, CatBoostRegressor
import pandas as pd
import matplotlib.pyplot as plt

# initialize data
df = pd.read_csv('data.csv')
feature_cols = df.columns.drop(['salary', 'salary_in_usd'])
train_data = df[feature_cols]
train_label = df['salary']

categorical_cols = [col for col in feature_cols if df[col].dtype == 'object']
train_pool = Pool(train_data,train_label,cat_features=categorical_cols)
model = CatBoostRegressor(iterations=30000,
                          depth=6,
                          learning_rate=0.04,
                          loss_function='RMSE',
                          task_type='GPU')
model.fit(train_pool)
model.save_model('model.cbm')