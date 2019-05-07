# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

_list = []
sum = 0
while True:
  input_list = [int(x) for x in input('Please input a number(press enter to stop):\n').split()]
  if not input_list:
    break
  _list += input_list

for i in range(len(_list)):
  sum += _list[i] 

print(f'Sum: {sum}, Average: {sum/len(_list)}')
