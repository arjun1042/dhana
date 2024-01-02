#factorial
def fact(n):
    f=1
    while n>=1:
        f=f+n
        n=n-1
    return f
n=int(input("enter a number to calculate factorial"))
fact=fact(n)
print("factorial=",fact)
    
    
 
