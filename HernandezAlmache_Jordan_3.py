
#Jordan Hernandez-Alamche
#CSci 161 L03
#Assignment 3

#Ask user to enter two numeric values,
#1 Both values must be stored as minimum and maximum values. Use assert syntax to check if the 
#  second value is larger than the first value.
#2 Print the odd numbers between those two values using the while loop.
#3 Print the prime numbers between those values using while loop.
#4 Using a for loop, print the number(s) between those values incrementing by 2.
#5 Print the numbers from the range mentioned above using for loop incrementing by 2 while
#  skipping the multiples of 3 by using continue.

max_value = int(input('Enter the maximum value:'))
min_value = int(input('Enter the minimum value:'))
assert (max_value > min_value),'Please enter a maximum value:'


print('Odd numbers within the range of {} and {}.'.format(min_value, max_value))
i = max_value
while i >= min_value:
    if  i % 2 != 0:
        print(i,end=' ')
    i -= 1 


print('\nPrime numbers within the range of {} and {}.'.format(min_value, max_value))
a = min_value
while a < max_value:
    count = 0 
    for j in range(2, a):
        if(a % j == 0):
            count = 1
            break
    if (count == 0):
        print(a, end = ' ')
    a += 1


print('\nIncrement numbers within the range of {} and {} by 2.'.format(min_value, max_value))
j = 0
for j in range(min_value, max_value, 2):
    print(j, end = ' ')


print('\nIncrement numbers within the range of {} and {},by 2 and skipping multiples of 3. '.format(min_value, max_value))
j = 0
for j in range(min_value, max_value, 2):
    if (j % 3 != 0):
        print(j, end = ' ')
    else:
        continue
#6 For this part please check the following:
#    a Assign a list of 10 diff. numeric values in your code that must include a 
#      value "5" (any 10 values, not entered by user)
#    b Find the product of all numbers in the list that occur before 5. Break the loop when 5 is found.
#    c Print the product value found in (Step b) and the index of the "5" in the list
#      ex.(Do not use this example in your code.)
#        List = [1,2,3,4,5,6,7,8,9,1]
#        Product = 24
#        Index found at 4.
#        (Note) The List should have 2-digit and 3-digit numbers as well and it must include a 5.

value_list = [13,1,9,46,87,5,8,97,6,132]
print('\nThe values in list are:\n', value_list)

j = 0
product = 1
flag = 0
for j in value_list:
    if j != 5:
        product = product * j 
        flag += 1
    else:
        break
print('Product =', product)
print('Index found at {}.'.format(flag))

