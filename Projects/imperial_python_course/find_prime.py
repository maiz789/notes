def read_integer():
    integer = int(input("Enter a number: "))
    return integer

def is_prime(num):
    i = 2
    while(i < (num/2)):
        if(num%i == 0):
            return False
        else:
            i = i + 1

    if(i > num/2 ):
        True

n = read_integer()
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")