from forest import Forest
from foxtail_pine import FoxtailPine
from whitebark_pine import WhitebarkPine
from lumberjack import Lumberjack


def test():
  tree_1 = FoxtailPine(10)
  tree_2 = FoxtailPine(4)
  tree_3 = WhitebarkPine(4)
  tree_4 = WhitebarkPine(6)

  forest = Forest([tree_1, tree_3])

  forest.add_tree(tree_2)
  forest.add_tree(tree_4)
  print('Before rain\n', forest.get_status())

  forest.rain()
  print('After rain\n', forest.get_status())

  lumberjack = Lumberjack()
  forest.cut_trees(lumberjack)
  print('After cut:\n ', forest.get_status())
  print('Is empty: \n', forest.is_empty())

test()