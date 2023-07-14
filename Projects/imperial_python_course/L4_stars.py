"""
rows = int(input("Enter number of rows: "))
count = 1
while count <= rows:
    print((2*count - 1) * "*")
    count += 1
"""
minute = 5

while minute > 0:
    print(minute)
    second = 60
    while second > 0:
        if second % 10 == 0:
            print(second) 
        second = second - 1
    minute = minute - 1
    if minute == 2:
        print("Almost there!")

print("Time's up!!")
