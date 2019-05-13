from aircraft import Aircraft

class F35(Aircraft):
  def __init__(self):
    super().__init__(12, 50)
  def getType(self):
    if isinstance(self, F35):
      return 'F35'
  def getStatus(self):
    return self.getType() + ' Ammo:'  + str(self.ammo) + ', Base Damage:' + str(self.base_damage) + ', All Damage: ' + str(self.get_all_damage())
  def isPriority(self):
    return True