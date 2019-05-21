from vegetation import Vegetation

class Flower(Vegetation):
  def __init__(self, color, water = 0):
    super().__init__(color, water)
  
  def absorb_water(self, water):
    self.water += 0.75 * water
  
  def need_water(self):
    return self.water < 5
  
  def __str__(self):
    if self.need_water():
      water_str = 'needs'
    else:
      water_str = 'doesn\'s need'
    return 'The ' + self.color + ' Flower ' + water_str + ' Water'