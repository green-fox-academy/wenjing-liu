from cows_and_bulls import CAB
import unittest

class TestCABMethods(unittest.TestCase):
  def setUp(self):
    self.cab = CAB()
  
  def test_init(self):
    self.assertEqual(self.cab.counter, 0)
    self.assertEqual(self.cab.state, 'not start')
    self.assertEqual(len(str(self.cab.number)), 4)
  
  def test_guess_four_cow(self):
    number = self.cab.number
    self.assertEqual(self.cab.guess(number), '4 cow, 0 bull')
    self.assertEqual(self.cab.state, 'finished')
  
  def test_guess_with_len_5(self):
    with self.assertRaises(ValueError):
      self.cab.guess(23456)
  
if __name__ == '__main__':
    unittest.main()