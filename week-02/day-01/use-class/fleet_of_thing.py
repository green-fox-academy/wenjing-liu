from fleet import Fleet
from thing import Thing

thing_1 = Thing('Get milk')
thing_2 = Thing('Remove the obstacles')
thing_3 = Thing('Stand up')
thing_3.complete()
thing_4 = Thing('Eat lunch')
thing_4.complete()

thing_list = [thing_1, thing_2, thing_3, thing_4]
fleet = Fleet()
for thing in thing_list:
  fleet.add(thing)

# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

print(fleet)

"""
# Fleet of Things
- You have the `Thing` class
- You have the `Fleet` class
- You have the `fleet_of_things.py` file
- Download those, use those
- In the `fleet_of_things` file create a fleet
- Achieve this output:
```
1. [ ] Get milk
2. [ ] Remove the obstacles
3. [x] Stand up
4. [x] Eat lunch
```
"""