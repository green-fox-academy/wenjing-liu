from f35 import F35
from f16 import F16

class AircraftCarrier: 
  def __init__(self, ammo_storage, health_point = 5000):
    self.aircrafts = []
    self.ammo_storage = ammo_storage
    self.health_point = health_point

  def add(self, aircraft):
    self.aircrafts.append(aircraft)
  def fill(self):
    if self.ammo_storage <= 0:
      raise Exception('You are out of ammo')
    
    ammoo_point = 0
    for index in range(len(self.aircrafts)):
      ammoo_point += self.aircrafts[index].max_ammo - self.aircrafts[index].ammo
    
    if self.ammo_storage < ammoo_point:
      all_priority_craft = []

      for i in range(len(self.aircrafts)):
        if self.aircrafts[index].isPriority():
          all_priority_craft.append(self.aircrafts[index])
      for j in range(len(all_priority_craft)):
        if self.ammo_storage > 0:
          self.ammo_storage -= (all_priority_craft[j].max_ammo - all_priority_craft[j].ammo)
        else:
          break
      if self.ammo_storage > 0:
        for i in range(len(self.aircrafts)):
          if self.ammo_storage > 0:
            self.ammo_storage -= self.aircrafts[j].max_ammo - self.aircrafts[j].ammo
          else:
            break
    else:
      for index in range(len(self.aircrafts)):
        self.aircrafts[index].ammo = self.aircrafts[index].max_ammo
  def fight(self, another_carrier):
    self.health_point -= another_carrier.get_total_damage()

  def get_total_damage(self):
    damage = 0
    for index in range(len(self.aircrafts)):
      damage += self.aircrafts[index].get_all_damage()
    return damage
  def get_status(self):
    if (self.health_point <= 0):
      return 'It\'s dead Jim'
    result = 'HP: ' + str(self.health_point) + ', Aircraft count: ' + str(len(self.aircrafts)) + ',  Ammo Storage: ' + str(self.ammo_storage) + ', Total damage: ' + str(self.get_total_damage()) + '\n'
    
    result += 'Aircrafts:\n'
    for index in range(len(self.aircrafts)):
      result += self.aircrafts[index].getStatus() + '\n'
    return result

f16_1 = F16()
f16_2 = F16()
f35_1 = F35()
f35_2 = F35()
f35_3 = F35()
aircraft_carrier = AircraftCarrier(2300)
aircraft_carrier.add(f16_1)
aircraft_carrier.add(f16_2)
aircraft_carrier.add(f35_1)
aircraft_carrier.add(f35_2)
aircraft_carrier.add(f35_3)
print(aircraft_carrier.get_status())
aircraft_carrier.fill()
print(aircraft_carrier.get_status())

f16_11 = F16()
f16_22 = F16()
f35_11 = F35()
aircraft_carrier_2 = AircraftCarrier(2300)
aircraft_carrier_2.add(f16_11)
aircraft_carrier_2.add(f16_22)
aircraft_carrier_2.add(f35_11)
aircraft_carrier_2.fill()

aircraft_carrier.fight(aircraft_carrier_2)
print(aircraft_carrier.get_status())



