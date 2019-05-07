# Write a program that asks for two numbers
# The first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people

girl_num, boy_num = [int(x) for x in input('Please input the numbers of girls and the numbers of boys to the party(press enter to end):\n').split()]

total_num = girl_num + boy_num
avg_total_num = 20

if girl_num == 0:
    print('Sausage party')
elif total_num < avg_total_num:
    print('Average party...')
elif (total_num > avg_total_num and girl_num != boy_num):
    print('Quite cool party!')
elif (total_num > avg_total_num and girl_num == boy_num):
    print('The party is exellent!')