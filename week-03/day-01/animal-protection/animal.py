class Animal:
  def __init__(self, name = 'Animal', health_state = True, heal_cost = 0):
    self.name = name
    self.is_healthy = health_state
    self.heal_cost = heal_cost
  
  def heal(self):
    self.is_healthy = True
  
  def is_adoptable(self):
    return self.is_healthy
  
  def to_string(self):
    if self.is_healthy:
      return f'{self.name} is healthy, and adoptable'
    else:
      return f'{self.name} not healthy ({self.heal_cost}), and not adoptable'


'''
#### Animal

- It must have `name` and stores it's `healthState` (true or false) and a `healCost`.
- It must have a method named `heal()`, that sets the `isHealthy` field's status to true
- It must have a method named `isAdoptable` that returns a boolean value whether it can be adopted or not     - an animal can be adopted if it is healthy
- It must have a method named `toString()` that represents the Animal in the following format:

```
<name> is not healthy (<heal cost>€), and not adoptable
<name> is healthy, and adoptable
```

*The animal's name is the same as the class name by default, but it can be set trough constructor as well*
'''