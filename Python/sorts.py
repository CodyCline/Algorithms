#Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for x in range(0, n - i - 1): #subtraction
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
    print(arr)

#Selection sort
def selection_sort(arr):
   for fillslot in range(len(arr)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if arr[location] > arr[positionOfMax]:
               positionOfMax = location

       temp = arr[fillslot]
       arr[fillslot] = arr[positionOfMax]
       arr[positionOfMax] = temp
       print(arr)


def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
     print(alist)


def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)
        

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   print(alist)
   return rightmark
   



''' Called upon functions '''

#bubble_sort([3261462314612346,11, 2342, 235, 25325])
#selection_sort([54,26,93,17,77,31,44,55,20])
#insertionSort([54,26,93,17,77,31,44,55,20])
#mergeSort([54,26,93,17,77,31,44,55,20])
quickSort([54,26,93,17,77,31,44,55,20])