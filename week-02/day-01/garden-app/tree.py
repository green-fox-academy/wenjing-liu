from vegetation import Vegetation

class Tree(Vegetation):
  def __init__(self, color, water = 0):
    super().__init__(color, water)
  def absorb_water(self, water):
    self.water += 0.4 * water
  def need_water(self):
    if self.water < 10:
      return True
    else:
      return False
  def __str__(self):
    if self.need_water():
      water_str = 'needs'
    else:
      water_str = 'doesn\'s need'
    return 'The ' + self.color + ' Tree ' + water_str + ' Water'