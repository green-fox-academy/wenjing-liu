from tree import Tree

class WhitebarkPine(Tree):
  def __init__(self, height = 0):
    super(WhitebarkPine, self).__init__(height)
  
  def irrigate(self):
    self.height += 2



'''
##### WhitebarkPine

- This tree type grows by 2 units each time its irrigated.
'''