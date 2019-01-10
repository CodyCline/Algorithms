'''
Simple arithmetic operations, loops
'''


#Loop 1-255
for i in range(1,256):
   print(i)

#Loop 1-255 even only
for i in range(1,256):
   if i % 2 == 0:
       print(i)

#Loop 1-255 odd only
for i in range(1, 256):
    if i % 2 != 0:
        print(i)

#FizzBuzz: Counting from 1-255 print 'fizz' if factor of 3; print 'buzz'
#  if factor of 5; print 'fizzbuzz' if factor of both 3 and 5.
for i in range(1, 256):
    if i % 3 == 0:
        print('fizz', i)
    if i % 5 == 0: 
        print('buzz', i)
    if i % 5 == 0 and i % 3 == 0:
        print('fizzbuzz', i)


#Find max in list
def find_max(input_nums):
    max = input_nums[0]
    print('Finding maximum in this list => ', input_nums)
    for i in input_nums:
        if i > max:
            max = i 
    print('The max in the list is ', max)
    return max

#Find minimum in a list
def find_min(input_nums):
    min = input_nums[0]
    print('Finding the minimum in this list =>', input_nums)
    for i in input_nums:
        if i < min: 
            min = i
    print('The min in the list is ', min)
    return min

#Get range of list
def find_range(input_nums):
    max = find_max(input_nums)
    min = find_min(input_nums)
    range = max - min
    print("The range is ", range)

#Get average of a list
def average(the_list):
    sum = 0 
    count = len(the_list)
    for i in range(0, count):
        sum += the_list[i]
    print("The average is ", sum/count)

#Median of list -- the number thats in the middle
def median(input_list):
    sorted_list = sorted(input_list)
    #first = 0
    first = sorted_list[0]
    last = len(sorted_list) - 1
    midpoint = (first + last) / 2
    print ('The midpoint is ', midpoint)
    return midpoint

def factorial(input_num):
    factorial_scale = 1
    if input_num < 0: 
        print("Negative numbers are not allowed")
    elif input_num == 0:
        print(1)
        return 1
    else:
        for i in range(1, input_num + 1):
            factorial_scale = factorial_scale * i
    print('The factorial is of {} is {}'.format(input_num, factorial_scale))
    return factorial
factorial(4)
