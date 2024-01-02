known_users=["ravi","ashu","jumba","kamesh","paul","rakesh","king"]

while True:
    name=input("what is your name? :")
    if name in known_users:
        print("hello {}!".format(name))
        remove =input("would you like to be remove from the system (y/n)?:" )
       
    else:
        print("name NOT recognised")

    
