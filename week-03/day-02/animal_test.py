from animal import Animal
import unittest

class TestAnimalMethods(unittest.TestCase):
  def setUp(self):
    self.animal = Animal()
  
  def test_eat(self):
    self.animal.eat()
    self.assertEqual(self.animal.hunger, 49)
  def test_drink(self):
    self.animal.drink()
    self.assertEqual(self.animal.thirst, 49)
  def test_play(self):
    self.animal.play()
    self.assertEqual(self.animal.hunger, 51)
    self.assertEqual(self.animal.thirst, 51)
  
  def test_str_(self):
    self.assertEqual(str(self.animal), '50, 50')



if __name__ == '__main__':
  unittest.main()



'''
# Animal

- Search back in your own project directory the [Animal](../../oo/animal) class
  you made on the OO workshop
- Create tests for multiple test cases.
'''