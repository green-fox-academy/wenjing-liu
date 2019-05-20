from marvel_hero import MarvelHero
from dc_hero import DCHero
from hero import Hero

def test():
  dc_hero = DCHero('Claire')
  marvel_hero = MarvelHero('Bob')
  dc_hero.punch(marvel_hero)
  print(dc_hero.to_string())
  print(marvel_hero.to_string())


test()