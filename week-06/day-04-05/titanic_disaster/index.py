

#%%
import pandas as pd
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing, metrics, neighbors, tree, naive_bayes, svm, ensemble
from sklearn.model_selection import cross_val_predict, train_test_split

used_features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
def load_csv_data(path):
  return pd.read_csv(path)

#%%
# FEATURE ENGINEERING
def scaler_age_fare(data):
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
  df = scaler_age_fare(df)
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
def clean_feature(train_data, test_data):
  # Data Cleaning
  cleaned_train_data = data_cleaning(train_data)
  cleaned_test_data = data_cleaning(test_data)

  # Feature Engineering
  featured_train_data = feature_engineering(cleaned_train_data)
  featured_test_data = feature_engineering(cleaned_test_data)
  return [featured_train_data, featured_test_data]



#%%
# Use linear regression model
def train_linear_model():
  # Data Acquisition
  raw_train_data = load_csv_data('train.csv')
  raw_test_data = load_csv_data('test.csv')

  [train_data, test_data] = clean_feature(raw_train_data, raw_test_data)
  
  # Get xs and y
  train_xs_data = train_data.drop('Survived', axis=1)
  train_target = train_data['Survived']
  
  # Use linear model
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)
  lr_model = linear_model.LinearRegression()
  lr_model.fit(X_train, y_train)
  
  score = lr_model.score(X_test, y_test)
  predict_result = lr_model.predict(test_data)
  print("Linear regression Accuracy:{0:.3f}".format(score),"\n")

# train_linear_model()

#%%
# K nearest neighbor regression
def train_neighbors_model():
  # Data Acquisition
  raw_train_data = load_csv_data('train.csv')
  raw_test_data = load_csv_data('test.csv')

  [train_data, test_data] = clean_feature(raw_train_data, raw_test_data)
  
  # Get xs and y
  train_xs_data = train_data.drop('Survived', axis=1)
  train_target = train_data['Survived']
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)

  n_neighbors = 7
  # we create an instance of Neighbours Classifier and fit the data.
  neigh = neighbors.KNeighborsClassifier(n_neighbors)
  neigh.fit(X_train, y_train)
  score = neigh.score(X_test, y_test)
  raw_test_data['Survived'] = pd.Series(neigh.predict(test_data))
  result = raw_test_data[['PassengerId', 'Survived']]
  result.to_csv('7_neighbor_nearest_result.csv', index=False)
  print("7-nearest-neighbors Accuracy:{0:.3f}".format(score),"\n")

# train_neighbors_model()

#%%
# Decision Trees

def train_decision_tree():
  # Data Acquisition
  raw_train_data = load_csv_data('train.csv')
  raw_test_data = load_csv_data('test.csv')

  [train_data, test_data] = clean_feature(raw_train_data, raw_test_data)
  
  # Get xs and y
  train_xs_data = train_data.drop('Survived', axis=1)
  train_target = train_data['Survived']
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)

  dtree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3,min_samples_leaf=5)
  dtree = dtree.fit(X_train, y_train)
  y_test_pred = dtree.predict(X_test)
  print("Decision_tree Accuracy:{0:.3f}".format(metrics.accuracy_score(y_test,y_test_pred)),"\n")
  raw_test_data['Survived'] = pd.Series(dtree.predict(test_data))
  result = raw_test_data[['PassengerId', 'Survived']]
  result.to_csv('decision_tree_result.csv', index=False)

# train_decision_tree()

#%%
# Logistic Regression 
def train_logistic_regression():
  # Data Acquisition
  raw_train_data = load_csv_data('train.csv')
  raw_test_data = load_csv_data('test.csv')

  [train_data, test_data] = clean_feature(raw_train_data, raw_test_data)
  
  # Get xs and y
  train_xs_data = train_data.drop('Survived', axis=1)
  train_target = train_data['Survived']
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)

  logisticRegr = linear_model.LogisticRegression()
  logisticRegr.fit(X_train, y_train)
  score = logisticRegr.score(X_test, y_test)
  print("Linear regression Accuracy:{0:.3f}".format(score),"\n")
  raw_test_data['Survived'] = pd.Series(logisticRegr.predict(test_data))
  result = raw_test_data[['PassengerId', 'Survived']]
  result.to_csv('logistic_regression_result.csv', index=False)


# train_logistic_regression()

#%%
def train_gaussian_naive_bayes():
  # Data Acquisition
  raw_train_data = load_csv_data('train.csv')
  raw_test_data = load_csv_data('test.csv')

  [train_data, test_data] = clean_feature(raw_train_data, raw_test_data)
  
  # Get xs and y
  train_xs_data = train_data.drop('Survived', axis=1)
  train_target = train_data['Survived']
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)
  gnb = naive_bayes.GaussianNB()
  gnb.fit(X_train, y_train)  
  y_test_pre = gnb.predict(X_test)
  print("Gaussian naive bayes Accuracy:",metrics.accuracy_score(y_test, y_test_pre))
  
  raw_test_data['Survived'] = pd.Series(gnb.predict(test_data))
  result = raw_test_data[['PassengerId', 'Survived']]
  result.to_csv('gaussian_naive_bayes_result.csv', index=False)

# train_gaussian_naive_bayes()

#%%
# svm

def train_svm():
  # Data Acquisition
  raw_train_data = load_csv_data('train.csv')
  raw_test_data = load_csv_data('test.csv')

  [train_data, test_data] = clean_feature(raw_train_data, raw_test_data)
  
  # Get xs and y
  train_xs_data = train_data.drop('Survived', axis=1)
  train_target = train_data['Survived']
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)

  svmclf =  svm.SVC(gamma='auto')
  svmclf.fit(X_train, y_train)
  y_test_pred = svmclf.predict(X_test)
  print("SVM Accuracy:",metrics.accuracy_score(y_test, y_test_pred))

  raw_test_data['Survived'] = pd.Series(svmclf.predict(test_data))
  result = raw_test_data[['PassengerId', 'Survived']]
  result.to_csv('svm_result.csv', index=False)

# train_svm()

#%%
# Random Forest

def train_random_forest():
  # Data Acquisition
  raw_train_data = load_csv_data('train.csv')
  raw_test_data = load_csv_data('test.csv')

  [train_data, test_data] = clean_feature(raw_train_data, raw_test_data)
  
  # Get xs and y
  train_xs_data = train_data.drop('Survived', axis=1)
  train_target = train_data['Survived']
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)

  rfclf = ensemble.RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
  rfclf.fit(X_train, y_train)
  y_test_pred = rfclf.predict(X_test)
  print("Random Forest  Accuracy:",metrics.accuracy_score(y_test, y_test_pred))

  raw_test_data['Survived'] = pd.Series(rfclf.predict(test_data))
  result = raw_test_data[['PassengerId', 'Survived']]
  result.to_csv('random_forest_result.csv', index=False)

# train_random_forest()