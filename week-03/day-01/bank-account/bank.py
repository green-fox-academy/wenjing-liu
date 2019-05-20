from bank_account import BankAccount

class Bank:
  def __init__(self):
    self.bank_account_list = []
  def create_account(self, bank_account):
    if not isinstance(bank_account, BankAccount):
      raise Exception('Please add an BankAcount')
    self.bank_account_list.append(bank_account)
  
  def get_all_money(self):
    total_money = 0
    for account in self.bank_account_list:
      total_money += account.currency.value
    return total_money



'''
## Bank

- It must have a `BankAccount` list.
- It must have a `createAccount` method with a BankAccount as an input parameter
  - it must add the `BankAccount` to the list
- It should have a `getAllMoney` method, which returns the sum of
  - the accounts' money (sum of Currency values regardless of the Currency type).
'''