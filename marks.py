#nested if program
s1=int(input("enter marks"))
s2=int(input("enter marks"))
s3=int(input("enter marks"))
s4=int(input("enter marks"))
total=s1+s2+s3+s4
print(total)
if total>=300:
  print("grade a")
if s1>=35 and s2>=35 and s3>=35 and s4>=35:
    print("pass ")
    if total>400:
         print("garade A")
    elif total>=300:
             print("b")
else:
    print("fail")
