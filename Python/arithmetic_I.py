'''
Simple arithmetic operations, loops
'''


#Loop 1-255
for x in range(1,256):
    print(x)

#Loop 1-255 even only
for i in range(1,256):
    if i % 2 == 0:
        print(x)

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
    for x in input_nums:
        if x > max:
            max = x 
    print('The max in the list is ', max)

find_max([1, 2, 6 ,18 ,2, 125])

#Get range of list

#Get average of a list
avg_list = [10, 15, 125, 13, 22.56] 
def average(the_list):
    sum = 0 
    count = len(the_list)
    for i in range(0, count):
        sum += the_list[i]
    print("The average is ", sum/count)

