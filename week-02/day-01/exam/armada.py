from ship import Ship

class Armada:
  def __init__(self):
    self.ship_list = []

  def add(self, ship):
    self.ship_list.append(ship)

  def war(self, other_armada):
    i, j = 0, 0
    while i < len(self.ship_list) and j < len(other_armada.ship_list):
      if (self.ship_list[i].battle(other_armada.ship_list[j])):
        j += 1
      else:
        i += 1
    if i < len(self.ship_list):
      return True
    else:
      return False