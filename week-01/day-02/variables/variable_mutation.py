a = 3
# make the "a" variable's value bigger by 10
a += 10
print(a)

b = 100
# make b smaller by 7
b %= 7

print(b)

c = 44
# please double c's value
c *= 2

print(c)

d = 125
# please divide by 5 d's value
d /= 5

print(d)

e = 8
# please cube of e's value
e = e**3
print(e)

f1 = 123
f2 = 345
# tell if f1 is bigger than f2 (pras a boolean)
is_f1_bigger = f1 > f2
if is_f1_bigger:
    print(f'{f1} is bigger than {f2}')
else:
    print(f'{f1} is not bigger than {f2}')

g1 = 350
g2 = 200
# tell if the double of g2 is bigger than g1 (pras a boolean)
is_double_g2_bigger = (g2 * 2) > g1
if is_double_g2_bigger:
    print(f'Double {g2} is bigger than {g1}')
else:
    print(f'Double {g2} is not bigger thant {g1}') 


h = 1357988018575474
# tell if 11 is a divisor of h (pras a boolean)
is_a_divisor = (h % 11) == 0
if is_a_divisor:
    print(f'11 is a divisor of {h}')
else:
    print(f'11 is not a divisor of {h}')


i1 = 10
i2 = 3
# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)
is_i1_in_range = (i1 > i2 * i2) and (i1 < i2**3)
if is_i1_in_range:
    print(f'{i1} is higher than {i2} squared and smaller than {i2} cubed')
else:
    print(f'{i1} is not in the range')

j = 1521
# tell if j is divisible by 3 or 5 (pras a boolean)
is_divisible = (j % 3 == 0) or (j % 5 == 0)
if is_divisible:
    print(f'{j} is divisible by 3 or 5')

# print(k)