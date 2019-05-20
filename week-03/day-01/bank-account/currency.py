# import abc

class Currency:
  def __init__(self, value, code, central_bank_name):
    self.value = value
    self.code = code
    self.central_bank_name = central_bank_name
  def add(self, amount):
    if amount >= 0:
      self.value += amount
    return self.value
  def sub(self, amount):
    if amount > 0 and amount < self.value:
      self.value -= amount
      return amount
    else:
      return 0

'''
class Currency(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractproperty
  def value(self):
    return 'Abstract value'
  
  @value.setter
  def value(self, new_value):
    return 

  @abc.abstractproperty
  def code(self):
    return 'Absctract code'
  
  @code.setter
  def code(self, new_code):
    return 'Absctract code'
  
  @abc.abstractproperty
  def central_bank_name(self):
    return 'Abstract central bank name'
  @central_bank_name.setter
  def central_bank_name(self, new_value):
    return 'Abstract central bank name'

  # @abc.abstractmethod
  def add(self, amount):
    return
  # @abc.abstractmethod
  def sub(self, amount):
    return


'''

'''
## Currency

**Currency is an abstract class**

- It must have a code, a central bank name and a value field.

'''