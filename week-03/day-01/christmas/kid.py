class Kid:
  def __init__(self, name, age, is_good = True):
    self.name = name
    self.age = age
    self.is_good = is_good
    self.is_happy = False
  def get_a_gift(self):
    self.is_happy = True
  def introduce(self):
    happy_status = 'happy!'
    if not self.is_happy:
      happy_status = 'not happy.'
    return f'My name is {self.name}, I am {self.age} years old. I am {happy_status}'



'''
#### Kid

```
Properties
- name
- age
- is good
- is happy

Behaviour
- get a gift
  - it should make the Kid happy
- introduce
  - should return information about the kid
  - example 1:  "My name is Bob, I am 10 years old. I am happy!"
  - example 2:  "My name is Alice, I am 12 years old. I am not happy."
```

We should be able to create new Kids by providing the `name`, `age` and whether it is `good`. Every kid is **not happy** by default.
'''