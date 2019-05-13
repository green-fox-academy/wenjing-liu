import random

class DiceSet(object):

    def __init__(self):
        self.dices = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dices)):
            self.dices[i] = random.randint(1, 6)
        return self.dices

    def get_current(self, index = None):
        if index != None:
            return self.dices[index]
        else:
            return self.dices

    def reroll(self, index = None):
        if index != None:
            self.dices[index] = random.randint(1, 6)
        else:
            self.roll()


dice_set = DiceSet()
print(dice_set.get_current())
dice_set.roll()
for index in range(len(dice_set.get_current())):
  while(dice_set.get_current(index) != 6):
    dice_set.reroll(index)

print(dice_set.get_current())


"""
# DiceSet

- You have a `DiceSet` class which has 6 dices
- You can roll all of them with `roll()`
- Check the current rolled numbers with `get_current()`
- You can reroll with `reroll()`
- Your task is to roll the dices until all of the dices are 6
"""