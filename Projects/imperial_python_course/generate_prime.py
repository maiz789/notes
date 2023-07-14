def read_integer():
    integer = int(input("Enter a number: "))
    return integer

def is_prime(num):
    if num == 1:
        return False
    i = 2
    while(i <= (num/2)):
        if(num%i == 0):
            return False
        else:
            i = i + 1

    if(i > num/2 ):
        return True

max_number = read_integer()
current_value = 2
while current_value <= max_number:
    if is_prime(current_value):
        print(f"{current_value} is a prime number.")
    current_value += 1
print("max number reached")