class Animal:
  def __init__(self):
    self.hunger = 50
    self.thirst = 50
  
  def eat(self):
    if (self.hunger > 0):
      self.hunger -= 1
    else:
      print('You have eat all. Please play to increase your hunger.')
  def drink(self):
    if (self.thirst > 0):
      self.thirst -= 1
    else:
      print('You have drink all. Please play to increase you thirst.')
  def play(self):
    self.hunger += 1
    self.thirst += 1

animal_1 = Animal()
animal_2 = Animal()

animal_1.drink()
animal_1.eat()
print(animal_1.thirst)
print(animal_1.hunger)

for i in range(50):
  animal_2.eat()
  animal_2.drink()

animal_2.drink()
animal_2.eat()

animal_2.play()
print(animal_2.hunger)
print(animal_2.thirst)


"""
# Animal

 -  Create an `Animal` class
     -  Every animal has a `hunger` value, which is a whole number
     -  Every animal has a `thirst` value, which is a whole number
     -  when creating a new animal object these values are created with the default `50` value
     -  Every animal can `eat()` which decreases their hunger by one
     -  Every animal can `drink()` which decreases their thirst by one
     -  Every animal can `play()` which increases both by one
"""