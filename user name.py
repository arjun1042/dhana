#google form
while 'false':
    user_name=input("enter username")
    password=input("enter password")
    if user_name=="admin" and password=="admin":
        print("login success")
        break
    else:
            print("login denied")
            continue
