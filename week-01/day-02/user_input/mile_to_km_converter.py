# Write a program that asks for an integer that is a distance in miles,
# then it converts that value to kilometers and prints it
distance = int(input('Please input a distance in miles(press enter to end): '))
distance_in_km = distance / 1000
print(f'The distance of your input is {distance_in_km} km')