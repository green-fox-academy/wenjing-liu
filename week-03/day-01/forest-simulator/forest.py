from tree import Tree
from whitebark_pine import WhitebarkPine
from foxtail_pine import FoxtailPine
from lumberjack import Lumberjack

class Forest:
  def __init__(self, tree_list = []):
    self.tree_list = tree_list
  
  def add_tree(self, tree):
    self.tree_list.append(tree)
  
  def rain(self):
    for tree in self.tree_list:
      tree.irrigate()
  
  def cut_trees(self, lumberjack):
    left_tree_list = []
    for index in range(len(self.tree_list)):
      if not lumberjack.can_cut(self.tree_list[index]):
        left_tree_list.append(self.tree_list[index])
    self.tree_list = left_tree_list
  def is_empty(self):
    if len(self.tree_list):
      return False
    else:
      return True
  
  def get_status(self):
    result = ''
    for tree in self.tree_list:
      type_str = None
      if isinstance(tree, WhitebarkPine):
        type_str = 'WhitebarkPine'
      else:
        type_str = 'FoxtailPine'
      result += f'There is a {tree.get_height()} tall {type_str} in the forest.\n'
    return result
  

'''
#### Forest

- It should have a list of trees.
- We should be able to create a forest by providing the trees that live there.
- It must have a `rain` which should iterate through the trees and irrigate them one by one.
- It must have a `cutTrees(lumberjack)` which should remove all the trees which can be cut by the lumberjack. (It calls the `canCut` method on the lumberjack).
- It must have an `isEmpty` method which returns true if there is no tree in the forest.
- It must have a `getStatus` method which returns an array with status reports about each tree in the forest. eg.:

```
[
  'There is a 3 tall WhitebarkPine in the forest.',
  'There is a 2 tall WhitebarkPine in the forest.',
  'There is a 4 tall FoxtailPine in the forest.'
]
'''