

## Steps:
1. Grap data from `https://api.zoopla.co.uk/api/v1/property_listings`
2. Clean Data: remove non-numeric data, NaNs, and outliers (everything above 3 x standard dev of y)
3. Feature Engineering: 
4. do some simple data exploration / visualisation
5. define explanatory variables (surface,latitude,and longitude) and independent variable (price EUR)
6. split the data in train and test sets (+ normalise independent variables where required)
7. find the optimal model parameters using scikit-learn's GridSearchCV
8. fit the model using GridSearchCV's optimal parameters
9. evaluate estimator performance by means of 5 fold 'shuffled' nested cross-validation
10. predict cross validated estimates of y for each data point and plot on scatter diagram vs true y






# For reference: https://github.com/MBKraus/Predicting_real_estate_prices_using_scikit-learn

## 
##https://api.zoopla.co.uk/api/v1/property_listings.json?page_number=1&page_size=100&listing_status=sale&include_sold=1&area=Somerset&county=somerset&api_key=9dud55d9tr4ptf7umqt4rmf6