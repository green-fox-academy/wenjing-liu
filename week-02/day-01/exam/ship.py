from pirates import Pirates
import random

class Ship:
  def __init__(self):
    self.crew = []
    self.captain = None

  def fill_ship(self, captain, crew):
    self.captain = captain
    self.crew = crew
  def battle(self, other_ship):
    self_rum = self.captain.drink_times
    self_alive = self.counter_alive()
    other_rum = other_ship.captain.drink_times
    other_alive = other_ship.counter_alive()
    
    winner = self
    loser = other_ship
    if self_rum + self_alive < other_rum + other_alive:
      winner, loser = loser, winner
    random_rum = random.randint(0, len(winner.crew))
    winner.captain.drink_some_rum(random_rum)

    random_death = random.randint(0, loser.counter_alive())
    for index in range(random_death, 0, -1):
      for j in range(len(loser.crew)):
        if not loser.crew[j].is_died:
          loser.crew[j].die()
          break

    if winner == self:
      return True
    else:
      return False

  def counter_alive(self):
    counter_alive = 0
    for index in range(len(self.crew)):
      if not self.crew[index].is_died:
        counter_alive += 1
    return counter_alive 
  def __str__(self):
    string = 'Captains consumed rum: ' + str(self.captain.drink_times)
    if self.captain.is_died:
      string += ' and died'
    elif self.captain.pass_out:
      string += ' and passed out'
    else:
      string += ' and still can drink'

    return string + ' and ' + str(self.counter_alive()) + ' of alive pirates in the crew'
