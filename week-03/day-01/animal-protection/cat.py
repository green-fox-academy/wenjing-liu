from animal import Animal
import random

class Cat(Animal):
  def __init__(self, name = 'Cat', healthy = True):
    super(Cat, self).__init__(name, healthy, random.randint(0, 6))

'''
##### Cat

**`Cat` is an `Animal`**

-  The healing cost should be a random number between 0 and 6
'''