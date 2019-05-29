### Car dealer

Here is a car dealer's database in a [json file](./cars/cars.json). You should
migrate it into a postgres with python. After all the entries are migrated:

- Remove the cars which are not on stock
- Decrease the price of wrecks by 20%
- Count the average age of the cars on the stock