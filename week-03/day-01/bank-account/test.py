from bank_account import BankAccount
from bank import Bank
from currency import Currency
from usa_dollar import USADollar
from hungarian_forint import HungarianForint

def test():
  usa = USADollar(200)

  hungarian = HungarianForint(300)

  bank_account_usa = BankAccount('claire', '12345', usa)
  bank_account_hungarian = BankAccount('claire', '123456', hungarian)

  hua_bank = Bank()
  hua_bank.create_account(bank_account_usa)
  hua_bank.create_account(bank_account_hungarian)
  print(hua_bank.get_all_money())

test()