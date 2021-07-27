
#Jordan Hernandez-Alamche
#CSci 161 L03
#Assignment 2
'''
ask user for numeric value
a)the value entered is a whole number
b)the value is, or is not, a mult. of 7
c)the value is pos/neg/zero
d)the value is, or is not, within 2011-2021
e)the value is, or is not, within 1000's(4 digit's)(2 ways to accomplish)
'''
val1 = float(input('Please enter a numerical value:'))

if val1 % 1 == 0:
    print(val1,'is a whole number.')
else:
    print(val1,'is not a whole number.')

if val1 % 7 == 0:
    print(val1,'is a multiple of 7.')
else:
    print(val1,'is not a multiple of 7.')

if val1 > 0:
    print(val1,'is a positive number.')
elif val1 < 0:
    print(val1,'is a negative number.')
else:
    print(val1,'is zero.')

if val1 >= 2011 and val1 <= 2021:
    print(val1,'is within 2011 to 2021 inclusively.')
else:
    print(val1,'is NOT within 2011 to 2021 inclusively.')

if val1 >= 1000:
    print(val1,'is within the 1000\'s.')
else:
    print(val1,'is NOT within the 1000\'s.')

'''
ask for 2nd value. 
f)which of the 2 is smallest? or =
g)val2 is, or is not a mult of val1
h)val1 is, or is not a mult of val2
'''

val2 = float(input('Enter a second numerical value:'))

if val1 > val2:
    print('The second value ({1}) is smaller than the first value({0}).'.format(val1, val2))
elif val1 < val2:
    print('The first value ({0}) is smaller than the second value({1}).'.format(val1, val2))
else:
    print('The two values are equal.')

if val2 % val1 == 0:
    print('The second value ({1}) is a multiple of the fisrt value({0}).'.format(val1, val2))
else:
    print('The second value ({1}) is NOT a multiple of the fisrt value({0}).'.format(val1, val2))

if val1 % val2 == 0:
    print('The first value ({0}) is a multiple of the second value({1}).'.format(val1, val2))
else:
    print('The first value ({0}) is NOT a multiple of the second value({1}).'.format(val1, val2))
