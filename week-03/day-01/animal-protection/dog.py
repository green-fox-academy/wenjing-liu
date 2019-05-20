from animal import Animal
import random

class Dog(Animal):
  def __init__(self, name = 'Dog', healthy = True):
    super(Dog, self).__init__('Dog', healthy, random.randint(1, 8))
'''
##### Dog

**`Dog` is an `Animal`**

-  The healing cost should be a random number between 1 and 8
'''