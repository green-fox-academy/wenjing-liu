from currency import Currency

class HungarianForint(Currency):
  def __init__(self, value):
    super(HungarianForint, self).__init__(value, 'HUF', 'Hungarian National Bank')

'''
### HungarianForint

**`HungarianForint` is a `Currency`**

- It must accept a value.
- The code must be "HUF" by default.
- The central bank name must be "Hungarian National Bank" by default.
'''