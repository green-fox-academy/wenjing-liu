from hero import Hero

class DCHero(Hero):
  def __init__(self, name, motivation = 45):
    super(DCHero, self).__init__(name, motivation)

  def punch(self, other_hero):
    if isinstance(other_hero, DCHero):
      return
    Hero.punch(self, other_hero)

'''
##### DCHero

**`DCHero` is a `Hero`**
- It must have a default motivation 45 if the name is provided only.
- A DCHero shouldn't be able to punch another DCHero.
'''