from fish import Fish

class Clownfish(Fish):
  def __init__(self, name, color, weight):
    super(Clownfish, self).__init__(name, weight, 'stripe ' + color)

  def feed(self):
    self.weight += 1


'''
##### Clownfish

Clownfish, gains 1 gramm when feeded and has stripe color.
'''