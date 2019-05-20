# Bank Account

You are going to create a Bank Account where you can withdraw and deposit money.

## Currency

**Currency is an abstract class**

- It must have a code, a central bank name and a value field.

### USADollar

**`USADollar` is a `Currency`**

- It must accept a value.
- The code must be "USD" by default.
- The central bank name must be "Federal Reserve System" by default.

### HungarianForint

**`HungarianForint` is a `Currency`**

- It must accept a value.
- The code must be "HUF" by default.
- The central bank name must be "Hungarian National Bank" by default.

## BankAccount

- It must have a name a pin code and a Currency.
- It must have a `deposit` method that takes a `value` parameter
  - check if the given parameter is positive
  - then adds the parameter to the Currency's value field
- It must have a `withdraw` method with two parameters: a pin code and an amount
  - It must check if the given pin is correct (equals with the original pin)
  - and the Currency's value is more than the amount parameter
  - If so, subtract the amount from the Currency's value and return with the amount.
  - Otherwise don't modify the Currency's value and return with 0.

## Bank

- It must have a `BankAccount` list.
- It must have a `createAccount` method with a BankAccount as an input parameter
  - it must add the `BankAccount` to the list
- It should have a `getAllMoney` method, which returns the sum of
  - the accounts' money (sum of Currency values regardless of the Currency type).