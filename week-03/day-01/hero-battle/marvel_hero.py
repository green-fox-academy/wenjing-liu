from hero import Hero

class MarvelHero(Hero):
  def __init__(self, name, motivation = 40):
    super(MarvelHero, self).__init__(name, motivation)

  def punch(self, other_hero):
    if isinstance(other_hero, MarvelHero):
      return
    Hero.punch(self, other_hero)


'''
##### MarvelHero 

**`MarvelHero` is a `Hero`**
- It must have a default motivation 40 if the name is provided only.
- A MarvelHero shouldn't be able to punch another MarvelHero. 

**LET'S FIGHT BETWEEN THE SUPERHEROES**
'''