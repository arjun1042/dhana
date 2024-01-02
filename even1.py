#even numbers between two numbers
a=int(input("enter a value"))
b=int(input("enter b value"))
while a>=b:
    if a%2==0:
        print(a)
    a=a+1
