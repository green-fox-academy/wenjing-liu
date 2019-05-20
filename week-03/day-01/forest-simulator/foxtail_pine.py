from tree import Tree

class FoxtailPine(Tree):
  def __init__(self, height = 0):
    super(FoxtailPine, self).__init__(height)
  
  def irrigate(self):
    self.height += 1


'''
##### FoxtailPine

- This tree type grows by 1 unit each time its irrigated.
'''