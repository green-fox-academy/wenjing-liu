from tree import Tree

class Lumberjack(Tree):  
  def can_cut(self, tree):
    if tree.get_height() > 4:
      return True


'''
#### Lumberjack

You must be able to create a lumberjack without providing any parameters.

- It must have a `canCut(tree)` method which takes a tree as parameter and returns true if its taller than 4 units.
'''