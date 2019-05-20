### Candy shop

You are going to create a Candy shop where we sell candies and lollipops.

#### Sweet

**`Sweet` is an abstract class**

- It must have a type, a price and an amount of sugar.

##### Lollipop

**`Lollipop` is a `Sweet`**

- Its type is `lollipop`, price is 10$ and it made from 5gr of sugar.

##### Candie

**`Candie` is a `Sweet`**

- Its type is `candie` price is 20$ and it made from 10gr of sugar.

#### Candy shop

- It must have sugar, income, and an `inventory` (list of sweets).
- It should take an amount of sugar in gramms when creating an instance.
- It must have a `createSeet` method which takes `Sweet` as a parameter
  - and store it to the `inventory`
  - the `sugar` amount gets reduced by the amount needed to create the sweets
- It must have a `raise` method which takes an `amount` as a parameter
  - raise the prices of all the sweets in the `inventory` with the `amount`
- It must have a `sell` method which takes an `amount` and a `type` as parameter
  - the income will be increased by the price of the sweets and we delete it from the inventory
- It must have a `buySugar` method which takes an `amount` as parameter
  - price of 1000gr sugar is 100$
  - it must have raise the CandyShop's amount of sugar and reduce the income by the price of it
  - the income can't be below 0
- It must have a `toString` method which represents the Candy Shop
  - return a string in this format: "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"
        