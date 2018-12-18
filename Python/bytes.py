''' Chapter 2: Searches '''

#Search for a number in linear fashion
def linear_search(arr, key):
    for a in arr:
        if a == key:
            print ("FOUND")
        else:
            print("NOT FOUND")
    return True

#Sum of numbers
def iSum(num):
    sum = int()
    for n in range(0, num+1): #Because it's counting at index 1 instead of zero
        sum += n
    print("The iSum is ", sum)
    return True


#Iterative factorial
def iFactorial(num):
    sum=int()
    for n in range(0, num-1):
        sum *= n
        print(sum) 


#Recursive Factorial
def rFactorial( n ):
   if n < 1:   # base case
       return 1
   else:
       returnNumber = n * rFactorial( n - 1 )  # recursive call
       print(returnNumber)
       return returnNumber

def iFibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    print(a)
    return a

def rFibonacci(num):
    if num == 1 or num == 2:
        result = 1
        print(result)
    else:
        result = rFibonacci(num - 1) + rFibonacci(num - 2)
        print(result)
        return result
    
def binary_search_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid-1)
    # elem > arr[mid]
    return binary_search_recursive(arr, elem, mid+1, end)

def binary_search_iterative(arr, elem):
    start, end = 0, (len(arr) - 1)
    while start <= end:
        mid = (start + end) // 2
        if elem == arr[mid]:
            return mid
        if elem < arr[mid]:
            end = mid - 1
        else:  # elem > arr[mid]
            start = mid + 1

    return False




''' List of called functions '''

#linear_search([1, 3, 7, 7,8], 8) #input the set of numbers and the key
#iSum(5)
#iFactorial(5)
#rFactorial(5)
#iFibonacci(6)
#rFibonacci(6)
