import random

pass_out_time = 4
class Pirates:
  def __init__(self):
    self.drink_times = 0
    self.pass_out = False
    self.is_died = False

  def drink_some_rum(self, rum = 1):
    if self.check_died():
      return
    self.drink_times += rum

  def hows_it_going_mate(self):
    if self.check_died():
      return
    if (self.drink_times <=4):
      print('Pour me anudder!')
    else:
      print('Arghh, I\'ma Pirate. How d\'ya d\'ink its goin?')
      self.set_pass_out()

  def check_died(self):
    if self.is_died:
      print('he\'s dead')
      return True
    else:
      return False

  def set_pass_out(self):
    self.pass_out = True

  def die(self):
    self.is_died = True

  def brawl(self, x):
    if self.check_died() or x.check_died():
      return
    fighting_result = random.randint(0, 2)
    if fighting_result == 0:
      self.set_pass_out()
      x.set_pass_out()
    elif fighting_result == 1:
      self.die()
    else:
      x.die()

  def __str__(self):
    return 'Drink times: ' + str(self.drink_times) + '\n is pass_out: ' + str(self.pass_out) + '\n is died: ' + str(self.is_died)

pirate_1 = Pirates()
pirate_1.drink_some_rum()
pirate_1.drink_some_rum()
pirate_1.hows_it_going_mate()
pirate_1.drink_some_rum()
pirate_1.drink_some_rum()
pirate_1.drink_some_rum()
pirate_1.hows_it_going_mate()

pirate_1.die()
pirate_1.drink_some_rum()
pirate_1.hows_it_going_mate()


pirate_2 = Pirates()
pirate_2.drink_some_rum()
pirate_2.drink_some_rum()
pirate_2.drink_some_rum()
pirate_2.hows_it_going_mate()

pirate_3 = Pirates()
pirate_3.drink_some_rum()
pirate_3.drink_some_rum()
pirate_3.drink_some_rum()
pirate_3.hows_it_going_mate()

print('Pirate 2:', pirate_2)
print('Pirate 3: ', pirate_3)
pirate_2.brawl(pirate_3)
print('Pirate 2:', pirate_2)
print('Pirate 3: ', pirate_3)

