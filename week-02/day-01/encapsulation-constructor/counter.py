class Counter:
  def __init__(self, num = 0):
    self.num = int(num)
    self._initial_num = self.num
  def add(self, number = 1):
    if isinstance(number, (int, float)):
      self.num += int(number)
    else:
      raise Exception('You must input number')
  def get(self):
    return self.num
  def reset(self):
    self.num = self._initial_num
  
  

"""
# Counter
- Create `Counter` class
  - which has an integer field value
  - when creating it should have a default value 0 or we can specify it when creating
  - we can `add(number)` to this counter another whole number
  - or we can `add()` without parameters just increasing the counter's value by one
  - and we can `get()` the current value
  - also we can `reset()` the value to the initial value
- Check if everything is working fine with the proper test
  - Download `test_counter.py` and place it next to your solution
  - Run the test file as a usual python program
"""