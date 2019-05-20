class Hero:
  def __init__(self, name, motivation):
    self.name = name
    self.motivation = motivation
  
  def get_motivation_level(self):
    if self.motivation < 25:
      return 0
    elif self.motivation >= 25 and self.motivation <= 40:
      return 1
    else:
      return 2
  
  def punch(self, other_hero):
    if self.motivation > 1:
      other_hero.be_punched(self.motivation / 1.5)
  def be_punched(self, damage):
    self.motivation -= damage / self.motivation
  
  def to_string(self):
    level = self.get_motivation_level()
    if level == 0:
      return f'{self.name} is not motivated anymore.'
    elif level == 1:
      return f'{self.name} is motivated.'
    else:
      return f'{self.name} is well motivated.'

  

'''
#### Hero

- It must have a name.
- It must have a motivation: a number represents how much the hero wants to save the world
- It must set the motivation and name when creating an instance.
- It must have a `getMotivationLevel` method which returns a number between 0 and 2
  - 0 if the motivation below 25
  - 1 if the motivation between 25 and 40
  - 2 if motivation is above 40
- It must have a `punch` method which is take a damage on the **other hero** by using his/her `bePunched` function
  - damage = the puncher hero's motivation / 1.5
  - the hero punches other heroes only if his/her motivation level is at least 1
- It must have a `bePunched` method which takes a `damage` as a parameter
  - bePunched: the hero suffers damage, so his/her motivation decreases 
  - motivation = motivation - (damage / motivation)
- toString: returns a string status report about the hero
  - if the hero's motivation level is 0: {name} is not motivated anymore.
  - if the hero's motivation level is 1: {name} is motivated.
  - if the hero's motivation level is 2: {name} is well motivated.
'''