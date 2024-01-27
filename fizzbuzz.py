def fizzBuzz(n):

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
if __name__ == '__main__':
    
    n = int(input().strip())

    fizzBuzz(n)

"""

def fizzBuzz(n):
    # Write your code here
    for num in range(1,n+1):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
if __name__ == '__main__':
    
    n = int(input().strip())

    fizzBuzz(n)"""

