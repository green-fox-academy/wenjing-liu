from currency import Currency

class BankAccount:
  def __init__(self, name, pin_code, currency):
    if not isinstance(currency, Currency):
      raise Exception('Please put an Currency to the bank account')
    self.name = name
    self.pin_code = pin_code
    self.currency = currency
  
  def deposit(self, amount):
    return self.currency.add(amount)
  
  def withdraw(self, pin_code, amount):
    if pin_code !=self.pin_code:
      return 0
    return self.currency.sub(amount)
'''
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
'''