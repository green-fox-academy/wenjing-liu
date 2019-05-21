import unittest
from claire_work import Apple, Sum, is_anagram, counter_letters, fibonacci


class TestAppleMethods(unittest.TestCase):
  def setUp(self):
    self.apple = Apple()

  def test_str(self):
    self.assertEqual(self.apple.get_apple(), 'apple')

class TestSumMethods(unittest.TestCase):
  def setUp(self):
    self.sum = Sum()
  
  def test_sum_with_multiple_item_list(self):
    list = [1, 2, 3]
    self.assertEqual(self.sum.sum(list), 6)
  
  def test_sum_with_empty_list(self):
    list = []
    self.assertEqual(self.sum.sum(list), 0)
  
  def test_sum_with_one_item_list(self):
    list = [1]
    self.assertEqual(self.sum.sum(list), 1)
  
  def test_sum_with_not_number_item_in_list(self):
    list = [1, None, '2']
    with self.assertRaises(TypeError):
      self.sum.sum(list)

class TestIsAnagram(unittest.TestCase):
  def test_two_string_is_anagram(self):
    str_1 = 'customers'
    str_2 = 'store scum'
    self.assertTrue(is_anagram(str_1, str_2))
  
  def test_two_string_is_not_anagram(self):
    str_1 = 'green'
    str_2 = 'fox'
    self.assertFalse(is_anagram(str_1, str_2))


class TestCountLettersMethods(unittest.TestCase):
  def test_string_input(self):
    str_1 = 'aadd1'
    expceted_result = {'a': 2, 'd': 2, '1':1}
    self.assertDictEqual(counter_letters(str_1), expceted_result)


class TestFibonacciMethods(unittest.TestCase):
  def test_number_less_than_zero(self):
    number = -10
    with self.assertRaises(ValueError):
      fibonacci(number)
  
  def test_number_equal_to_1(self):
    number = 1
    self.assertEqual(fibonacci(number), [0])
  
  def test_number_bigger_than_1(self):
    self.assertEqual(fibonacci(2), [0, 1])
    self.assertEqual(fibonacci(2), [0, 1, 1])

      


        
  

if __name__ == '__main__':
  unittest.main()
