from kong import Kong
from tang import Tang
from clown_fish import Clownfish
from aquarium import Aquarium

def test():
  fish_tang = Tang('tang-1', 'blue', 20)
  fish_clown = Clownfish('clown-1', 'yellow', 4)
  fish_kong = Kong('kong-1', 'red', 6)
  aquarium = Aquarium()
  aquarium.add_fish(fish_tang)
  aquarium.add_fish(fish_clown)
  aquarium.add_fish(fish_kong)
  print('before feed:\n ', aquarium.get_status())
  aquarium.feed()
  print('After feed: \n', aquarium.get_status())
  aquarium.remove_big_fish()
  print('After remove big fish:\n', aquarium.get_status())

test()