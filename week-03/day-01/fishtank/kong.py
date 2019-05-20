from fish import Fish

class Kong(Fish):
  def __init__(self, name, color, weight):
    super(Kong, self).__init__(name, weight, color)
    
  def feed(self):
    self.weight += 2
'''
##### Kong

Koi, gains 2 gramms when feeded.
'''