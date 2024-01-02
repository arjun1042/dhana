units=int(input("enter units"))
if units>1 and units<=50:
    print(100)
elif units>100 and units<=150:
    print(units*3)
elif units>150 and units<=300:
    print(units*4)
else:
    print("enter valid number")
