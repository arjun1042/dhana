u=float(input("enter units"))
if u>0 and u<=50:
    print(100)
elif u>50 and u<=100:
     print(u*2.5)
elif u>100 and u<=200:
    print(u*3)
elif u>200 and u<=300:
    print(u*3.5)
elif u>300 and u<=400:
    print (u*4)
elif u>400:
    print(u*4.5)
else:
    print('enter valid input:')

