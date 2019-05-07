# Write a program that asks for two numbers and prints the bigger one
x, y = [int(z) for z in input('Please input two numbers(press enter to end):\n').split()]

if x > y:
    print(f'The bigger number is {x}')
else:
    print(f'The bigger number is {y}')
