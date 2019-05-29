### Car dealer

Here is a car dealer's database in a [json file](./cars/cars.json). You should
migrate it into a postgres with python. After all the entries are migrated:

- Remove the cars which are not on stock
- Decrease the price of wrecks by 20%
- Count the average age of the cars on the stock

### Get information about employees

Here you have [3 datasets](./employees), about a company's employees. Sad, but
the departments provided the data in different formats. You task is to
standardize and store them in database. Then you need to answer the following
questions:

- Which first name is the most common in the company?
- Which first name is the most common among the younger (<30) employees?
- What is the median salary in the company?
- How many employee earns more than the average?
  - do not hard-code the average
  - use one query
- Increase the salary by monthly $100 for everybody who earns less than the
median