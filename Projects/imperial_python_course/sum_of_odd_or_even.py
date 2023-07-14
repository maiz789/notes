num_cap = int(input("Enter a number: "))
if(num_cap%2 == 0):
    num = 0
    total = 0
else:
    num = 1
    total = 1
    
while(num < num_cap):
    num = num + 2
    total = total + num
    print(f"num: {num}")
print(f"sum is {total}")
