int_1 = int(input("Enter integer 1: "))
int_2 = int(input("Enter inetger 2: "))
int_3 = int(input("Enter inetger 3: "))

def compare_3_nums(a, b, c):
    if(a >= b) & ( a >= c):
        print(a)
    elif (b >= a) & (b >= c):
        print(b)
    else:
        print(c)
            
compare_3_nums(int_1, int_2, int_3)
#if int_1 == int_2 == int_3:
#    print("They are the same")
#elif int_1 > int_2:
#    print(int_1)
#else:
#    print(int_2)