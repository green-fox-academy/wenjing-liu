from currency import Currency


class USADollar(Currency):
  def __init__(self, value):
    super(USADollar, self).__init__(value, 'USD', 'Federal Reserve System')



'''
### USADollar

**`USADollar` is a `Currency`**

- It must accept a value.
- The code must be "USD" by default.
- The central bank name must be "Federal Reserve System" by default.
'''