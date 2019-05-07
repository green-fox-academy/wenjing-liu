# Write a program that reads a number from the standard input,
# Then prints "Odd" if the number is odd, or "Even" if it is even.

number = int(input('Please input a number(press enter to end):\n'))
is_even = number % 2 == 0

if is_even:
    print(f'{number} is even')
else:
    print(f'{number} is odd')