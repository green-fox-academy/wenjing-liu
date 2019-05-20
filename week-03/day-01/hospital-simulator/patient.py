import random
class Patient:
  def __init__(self, name):
    self.name = name
    self.severity = random.randint(1, 10)
  def treat(self):
    if self.severity > 1:
      self.severity -= 1
  def __str__(self):
    return f'{self.name}: {self.severity}'


'''
#### Patient class

The *Patient* class doesn't depend on any other classes.
It has two methods:

- One to retrieve the severity of the disease.
- One to treat the patient, it must decrease the severity by 1.

The severity is a random number between 1 and 10, you can set it in the
constructor or at the field declaration.
*Keep in mind, the severity cannot go below 0*
'''