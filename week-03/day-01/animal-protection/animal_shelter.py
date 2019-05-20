from animal import Animal
import random

class AnimalShelter:
  def __init__(self):
    self.budget = 50
    self.animal_list = []
    self.adopters = []
  
  def rescue(self, animal):
    if isinstance(animal, Animal):
      self.animal_list.append(animal)
    return len(self.animal_list)
  
  def heal(self):
    for index in range(len(self.animal_list)):
      if not self.animal_list[index].is_healthy and self.budget > self.animal_list[index].heal_cost:
        self.animal_list[index].is_healthy = True
        self.budget -= self.animal_list[index].heal_cost
        return 1
    return 0

  def add_adopter(self, adopter_name):
    self.adopters.append(adopter_name)
  
  def find_new_owner(self):
    random_index = random.randint(0, len(self.animal_list))
    find = False
    for index in range(random_index, len(self.animal_list)):
      if self.animal_list[random_index].is_healthy:
        self.animal_list.pop(index)
        find = True
        break
    if not find:
      for index in range(0, random_index):
        if self.animal_list[random_index].is_healthy:
          self.animal_list.pop(index)
          find = True
          break 
    if not find:
      return
    adopter_index = random.randint(0, len(self.adopters))
    self.adopters.pop(adopter_index)
  
  def earn_donation(self, amount):
    self.budget += amount
    return self.budget
  
  def to_string(self):
    to_string = f'Budget: {self.budget}€,\n There are {len(self.animal_list)} animal(s) and {len(self.adopters)} potential adopter(s)\n'
    for animal in self.animal_list:
      to_string += animal.to_string() + '\n'
    return to_string


'''
#### Animal shelter

- It must have a `budget`, an `animals` list, an `adopters` name list
- The shelter starts with 50€ without any Animal and adopter
- It must have a method named `rescue` this method takes an `Animal` as parameter 
  - and add the animal to the shelter's list and return the size of the list
- It must have a method named `heal` this method heals the first not healthy Animal
  - if it is possible by budget, returns the amount of healed animals(0 or 1)
- It must have a method named `addAdopter` this method takes a `name` as parameter 
  - and save it as a potential new owner
- It must have a method named `findNewOwner` 
  - this method pairs a random name with a random adoptable Animal if it is possible
  - and remove both of them from the lists
- It must have a method named `earnDonation` this method takes an `amount` as parameter 
  - and increase the shelter's budget by the parameter's value and returns the current budget
- It must have a method named `toString` that represents the shelter in the following format:

```
Budget: <budget>€, 
There are <animals.count> animal(s) and <potentionalAdopters.count> potential adopter(s)
<name> is not healthy (<heal cost>€), and not adoptable
<name> is healthy, and adoptable
```
'''