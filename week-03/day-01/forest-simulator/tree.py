import abc
class Tree(object):
  __metaclass__ = abc.ABCMeta
  def __init__(self, height = 0):
    self.height = height
  
  def get_height(self):
    return self.height
  
  @abc.abstractmethod
  def irrigate(self):
    return


'''
#### Tree

- Trees should have a height.
- We must be able to create trees in two ways:
  - providing `height`
  - not providing `height`, in this case the height will be 0 by default.
- It must have an `irrigate` method which will increase the height of the tree. It must be an abstract method and implementation should depend on the type of the tree.
- It must have a `getHeight` method which returns the tree's height.
'''