class Aircraft:
  def __init__(self, max_ammo, base_damage):
    self.ammo = 0
    self.max_ammo = max_ammo
    self.base_damage = base_damage

  def fight(self):
    damage = self.ammo * self.base_damage
    self.ammo = 0
    return damage

  def refill(self, amount_ammo):
    if amount_ammo + self.ammo > self.max_ammo:
      self.ammo = self.max_ammo
      return amount_ammo - (self.max_ammo - self.ammo)
    else: 
      self.ammo += amount_ammo
      return 0
  
  def get_all_damage(self):
    return self.ammo * self.base_damage
  
  def getType(self):
    if isinstance(self, Aircraft):
      return 'Aircraft'
  
  def getStatus(self):
    return self.getType() + ' Ammo:'  + str(self.ammo) + ', Base Damage:' + str(self.base_damage) + ', All Damage: ' + str(self.ammo*self.base_damage) 
