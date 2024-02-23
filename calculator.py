#calculator program in python
def addition(n1,n2):
    return n1+n2

def substraction(n1, n2):
    return n1-n2

def multiplication(n1, n2):
    return n1*n2

def division(n1,n2):
    return n1/n2


print("Operations")
print("press 1 for addition\n"
      "press 2 for subtraction\n"
      "press 3 for multiplication\n"
      "press 4 for division\n")

operation=int(input("Select an Option- "))



n1=float(input("enter 1st number"))
n2=float(input("enter 2nd nummber"))


if operation == 1:
    print (n1, "+", n2, "=", addition(n1, n2))

elif operation == 2:
    print (n1, "-", n2, "=", subtraction(n1, n2)) 

elif operation == 3:
    print (n1, "*", n2, "=", multiplication(n1, n2)) 
    
elif operation == 4:
    print (n1, "/", n2, "=", division(n1, n2)) 
    
else:
    print("wrong option you choosen")
