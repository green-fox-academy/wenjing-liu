

#%%
import pandas as pd
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing, metrics
from sklearn.model_selection import cross_val_predict, train_test_split

used_features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
def load_csv_data(path):
  return pd.read_csv(path)

#%%
# FEATURE ENGINEERING
def scaler_data(data):
  scaled_features = data
  col_names = ['Age', 'Fare']
  features = scaled_features[col_names]
  scaler = preprocessing.StandardScaler().fit(features.values)
  features = scaler.transform(features.values)
  scaled_features[col_names] = features
  return scaled_features

def feature_engineering(data):
  dummies_Sex = pd.get_dummies(data['Sex'], prefix= 'Sex')
  dummies_Pclass = pd.get_dummies(data['Pclass'], prefix= 'Pclass')
  df = pd.concat([data, dummies_Sex, dummies_Pclass], axis=1)
  df.drop(['PassengerId', 'Name', 'Ticket', 'Embarked', 'Cabin', 'Pclass', 'Sex'], axis=1, inplace=True)
  df = scaler_data(df)
  return df


#%%
# DATA CLEANING
def set_missing_age(data):
  missing_age_counter = data['Age'].isnull().count()
  avg_age = data['Age'].mean()
  std_age = data['Age'].std()
  random_age_arr = np.random.randint(avg_age - std_age, avg_age + std_age, size = missing_age_counter)
  data['Age'].fillna(pd.Series(random_age_arr), inplace = True)
  return data

def set_missing_fare(data):
  class_title_fare_grouping=data[['Pclass','Fare']].groupby(['Pclass']).median()
  for i in range(len(data.index)):
    for j in range(len(class_title_fare_grouping.index)):
      if (data.loc[i,'Pclass'])== class_title_fare_grouping.index[j] and np.isnan(data.loc[i,'Fare']):
          data.loc[i,'Fare']=class_title_fare_grouping.Fare[j]

  return data


def data_cleaning(data):
  data = set_missing_age(data)
  df = set_missing_fare(data)
  return df


#%%
# Drop the missing age data for 
def train_linear_model():
  # Data Acquisition
  train_data = load_csv_data('train.csv')
  test_data = load_csv_data('test.csv')

  # Data Cleaning
  cleaned_train_data = data_cleaning(train_data)
  cleaned_test_data = data_cleaning(test_data)

  # Feature Engineering
  featured_train_data = feature_engineering(cleaned_train_data)
  featured_test_data = feature_engineering(cleaned_test_data)
  
  # Get xs and y
  train_xs_data = featured_train_data.drop('Survived', axis=1)
  train_target = featured_train_data['Survived']
  
  # Use linear model
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)
  lr_model = linear_model.LinearRegression()
  lr_model.fit(X_train, y_train)
  
  score = lr_model.score(X_test, y_test)
  predict_result = lr_model.predict(featured_test_data)
  return predict_result, score

# print(train_linear_model())

#%%
