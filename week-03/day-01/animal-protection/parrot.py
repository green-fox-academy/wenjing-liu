from animal import Animal
import random

class Parrot(Animal):
  def __init__(self, name = 'Parrot', healthy = True):
    super(Parrot, self).__init__(name, healthy, random.randint(4, 10))

'''
##### Parrot

**`Parrow` is an `Animal`**

-  The healing cost should be a random number between 4 and 10
'''