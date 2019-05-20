import abc
class Fish(object):
  __metaclass__ = abc.ABCMeta

  def __init__(self, name, weight, color, short_term_memory_loss = False):
    self.name = name
    self.weight = weight
    self.color = color
    self.short_term_memory_loss = short_term_memory_loss
  
  def status(self):
    return (f'{self.name}, weight: {self.weight}, color: {self.color}, short-term memory loss: {self.short_term_memory_loss}')
  
  @abc.abstractmethod
  def feed(self):
    return
  

'''
#### Fish

Each fish has a name, weight and a color

- The fish has a status method it should print the status for a fish.
  - e.g.: `Dory, weight: 9, color: blue, short-term memory loss: true`
- The fish has an abstract feed method

**You can't instantiate a Fish**
'''