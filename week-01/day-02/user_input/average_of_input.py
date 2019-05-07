# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

number_list = [int(x) for x in (input('Please input five integers in a row (seperate by space)\n').split())]

print(f'Sum: {sum(number_list)}, Average: {sum(number_list) / len(number_list)}')
