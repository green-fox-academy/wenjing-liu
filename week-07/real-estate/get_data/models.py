from . import get_trainning_data
from statistics import mean
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing, metrics, neighbors, tree, naive_bayes, svm
from sklearn.model_selection import cross_val_predict, train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib

# score = 0.639
def train_linear_model():
  data = get_trainning_data()

  # Get xs and y
  train_xs_data = data.drop('price', axis=1)
  train_target = data['price']
  
  # Use linear model
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)
  lr_model = linear_model.LinearRegression()
  lr_model.fit(X_train, y_train)
  
  score = lr_model.score(X_test, y_test)
  print("Linear regression Accuracy:{0:.3f}".format(score),"\n")
  joblib.dump(lr_model, 'finalized_model.sav')

# train_linear_model()


# score = 0.661
def train_KNeighborsRegressor():
  data = get_trainning_data()

  # Get xs and y
  train_xs_data = data.drop('price', axis=1)
  train_target = data['price']
  
  # Use linear model
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)
  kng = KNeighborsRegressor(n_neighbors=10)
  kng.fit(X_train, y_train)
  score = kng.score(X_test, y_test)
  print("K Neighbors Regressor Accuracy:{0:.3f}".format(score),"\n")

# train_KNeighborsRegressor()


# score = 0.723
def train_RandomForestRegressor():
  data = get_trainning_data()

  # Get xs and y
  train_xs_data = data.drop('price', axis=1)
  train_target = data['price']
  
  # Use linear model
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)
  regr = RandomForestRegressor(max_depth=14, random_state=0, n_estimators=17)
  regr.fit(X_train, y_train)
  y_test_pre = regr.predict(X_test)
  print("Random Forest Regressor:",metrics.r2_score(y_test, y_test_pre))

# train_RandomForestRegressor()


