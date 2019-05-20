class Santa:
  def __init__(self, name, age, number_of_gifts = 100):
    self.name = name
    self.age = age
    self.number_of_gifts = number_of_gifts
  def introduce(self):
    gift_status = 'do not have any gifts'
    if self.number_of_gifts:
      gift_status = f'have {self.number_of_gifts} gifts'
    return f'My name is {self.name}, I am {self.age} years old. I {gift_status} in my bag.'
  def assign_gifts(self, kid_list):
    give_away_num = 0
    for kid in kid_list:
      if self.number_of_gifts > 0:
        if kid.is_good:
          kid.get_a_gift()
          self.number_of_gifts -= 1
          give_away_num += 1
      else:
        break
    return give_away_num




'''
#### Santa

```
Properties
- name
- age
- number of gifts

Behaviour
- introduce
  - should return information about the santa
  - example 1: "My name is Joe, I am 48 years old. I have 20 gifts in my bag."
  - example 2: "My name is Joe, I am 48 years old. I do not have any gifts in my bag."
- assign gifts
  - it should take a list of Kids as parameter
  - it should call each kid's `get a gift` behaviour if the kid is good and if Santa has any gifts left
  - if a gift is given, the `number of gifts` stored in Santa's bag should decrease (this cannot go under 0)
  - it should not do anything with the not good kids
  - in the end return the number of gifts which was given away
```

We should be able to create a new Santa by providing the `name` and `age`. The `number of gifts` should be 100 by default.
'''