from armada import Armada
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

ship_1 = Ship()
ship_1.fill_ship(pirate_1, [pirate_2, pirate_3])
print(ship_1)


pirate_4 = Pirates()
pirate_4.drink_some_rum(6)
pirate_4.hows_it_going_mate()
pirate_5 = Pirates()
pirate_5.drink_some_rum(3)
pirate_5.hows_it_going_mate()
pirate_6 = Pirates()
pirate_6.drink_some_rum(2)
pirate_6.hows_it_going_mate()
ship_2 = Ship()
ship_2.fill_ship(pirate_4, [pirate_5, pirate_6])

pirate_7 = Pirates()
pirate_7.drink_some_rum(1)
pirate_7.hows_it_going_mate()
pirate_8 = Pirates()
pirate_8.drink_some_rum(3)
pirate_8.hows_it_going_mate()
pirate_9 = Pirates()
pirate_9.drink_some_rum(2)
pirate_9.hows_it_going_mate()
ship_3 = Ship()
ship_3.fill_ship(pirate_7, [pirate_8, pirate_9])

pirate_10 = Pirates()
pirate_10.drink_some_rum(9)
pirate_10.hows_it_going_mate()
pirate_11 = Pirates()
pirate_11.drink_some_rum(7)
pirate_11.hows_it_going_mate()
pirate_12 = Pirates()
pirate_12.drink_some_rum(4)
pirate_12.hows_it_going_mate()
ship_4 = Ship()
ship_4.fill_ship(pirate_10, [pirate_11, pirate_12])

armada_1 = Armada()
armada_1.add(ship_1)
armada_1.add(ship_2)
armada_2 = Armada()
armada_2.add(ship_3)
armada_2.add(ship_4)

if armada_1.war(armada_2):
  print('======================')
  print('armada_1 win')
else:
  print('======================')
  print('armada_2 win')
