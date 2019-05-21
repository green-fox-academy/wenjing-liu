from sharpie import Sharpie
import unittest

class TestSharpieMethods(unittest.TestCase):
  def setUp(self):
    self.sharpie = Sharpie('blue', 100)
  
  def test_to_string_method(self):
    self.assertEqual(str(self.sharpie), 'blue sharpie with 100.0 has 100.0 ink amount')
  
  def test_use_amount_method(self):
    self.sharpie.use(20)
    self.assertEqual(self.sharpie.ink_amount, 80)
  
  def test_use_amount_method_with_not_number(self):
    with self.assertRaises(TypeError):
      self.sharpie.use('34')



if __name__ == '__main__':
  unittest.main()

