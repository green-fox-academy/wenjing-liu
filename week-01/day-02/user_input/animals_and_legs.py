# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs owned by the farmer
# It should print how many legs all the animals have

chick_count, pig_count = input('Please input the number of chickens and the number of pigs(use space to seperate values):\n').split()

chick_count = int(chick_count)
pig_count = int(pig_count)

print(f'{chick_count * 2 + pig_count * 4} legs all the animals have')