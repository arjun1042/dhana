def mul(n):
    for i in range(1,11):
        print("{multiplier}*{multiplicand}={multiplication}".format(
            multiplier=n, multiplicand=i, multiplication=n*i))

def main():
    n=int(input("Enter a Number: "))
    print(mul(n))
    
if __name__ == "__main__":
    main()
