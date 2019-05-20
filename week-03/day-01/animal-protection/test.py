from animal import Animal
from parrot import Parrot
from dog import Dog
from cat import Cat
from animal_shelter import AnimalShelter


def test():
  cat = Cat(healthy=False)
  dog = Dog()
  parrot = Parrot(healthy=False)
  animal_shelter = AnimalShelter()
  animal_shelter.add_adopter('Claire')
  animal_shelter.add_adopter('Bob')
  animal_shelter.rescue(cat)
  animal_shelter.rescue(dog)
  animal_shelter.rescue(parrot)
  print(animal_shelter.to_string())

  animal_shelter.find_new_owner()
  print(animal_shelter.to_string())

test()
