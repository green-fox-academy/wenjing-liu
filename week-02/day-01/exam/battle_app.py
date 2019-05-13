from pirates import Pirates
from ship import Ship

pirate_1 = Pirates()
pirate_1.drink_some_rum(5)
pirate_1.drink_some_rum()
pirate_1.hows_it_going_mate()
pirate_1.die()



pirate_2 = Pirates()
pirate_2.drink_some_rum(2)
pirate_2.hows_it_going_mate()

pirate_3 = Pirates()
pirate_3.drink_some_rum(2)
pirate_3.hows_it_going_mate()

print()
print('=====================')
ship = Ship()
ship.fill_ship(pirate_1, [pirate_2, pirate_3])
print(ship)


print()
print('=====================')
pirate_4 = Pirates()
pirate_4.drink_some_rum(6)
pirate_4.hows_it_going_mate()
ship_2 = Ship()
ship_2.fill_ship(pirate_4, [pirate_1, pirate_2, pirate_3])


if ship.battle(ship_2):
  print('The winner status is: ')
  print(ship)
else:
  print('The winner status is: ')
  print(ship_2)