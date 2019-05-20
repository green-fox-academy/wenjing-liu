from fish import Fish

class Tang(Fish):
  def __init__(self, name, color, weight):
    super(Tang, self).__init__(name, weight, color, True)
  def feed(self):
    self.weight += 1

'''
##### Tang

Tang, gains 1 gramms when feeded and can suffer short-term memory loss.
'''