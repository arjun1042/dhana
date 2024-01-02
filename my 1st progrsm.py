"""def bubbleSort(arr):
     
    n = len(arr)
 
    # For loop to traverse through all
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            #is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                 
# Driver code
 
# Example to test the above code
arr = [ 2, 1, 10, 23 ]
 
bubbleSort(arr)
 
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])"""


numbers = [1, 3, 4, 2]
 
# Sorting list of Integers
numbers.sort()
 
print(numbers)
 
# List of Floating point numbers
decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68]
 
# Sorting list of Floating point numbers
decimalnumber.sort()
 
print(decimalnumber)
 
# List of strings
words = ["Geeks", "For", "Geeks"]
 
# Sorting list of strings
words.sort()
 
print(words)
