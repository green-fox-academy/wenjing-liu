set_intro = {1}
print(type(set_intro))

set_intro.update([2, 3, 4, 5, 6])
print(set_intro)

set_intro.discard(2)
set_intro.discard(3)
print(set_intro)

for value in set_intro:
  print(value)

if 482 in set_intro:
  set_intro.remove()

set_intro.discard(42)

"""
# Set introduction

1. Create a set
1. Add at least 5 members to the set
1. Remove at most 2 members from the set
1. Iterate over the set and print its members
1. Remove 482 from the set if it is present
1. Remove 42 from the set even if it is not present

"""