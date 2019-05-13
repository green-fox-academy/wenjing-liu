from aircraft import Aircraft

class F16(Aircraft):
  def __init__(self):
    super().__init__(8, 30)
  def getType(self):
    if isinstance(self, F16):
      return 'F16'
  def getStatus(self):
    return self.getType() + ' Ammo:'  + str(self.ammo) + ', Base Damage:' + str(self.base_damage) + ', All Damage: ' + str(self.get_all_damage())
  def isPriority(self):
    return False
  