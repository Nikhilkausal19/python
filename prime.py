k=int(input("Enter any number"))
for n in range(2,k):
        if k%n==0:
            print(k,'is not a prime number')
            break
        else:
            print(k,'is a prime number')
            break
