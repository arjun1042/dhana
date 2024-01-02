
#find a number is prime or composite
n=int(input("enter prime or composite number"))
dhana=0
while n>=r:
 for r in range (1,n+1):
  if n%r==0:
   dhana=dhana+1
if dhana==2:
  print("prime number")
else:
    print("composite number")
