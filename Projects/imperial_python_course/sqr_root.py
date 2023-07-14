n_sqr = float(input("Please provide a number: "))
wanted_precision = 0.00001
#wanted_precision = float(input("Desired precision: "))
n_upper = n_sqr
n_lower = n_upper/2
max_iteration = 1000

def half(number):
    return number/2

while(n_lower**2 - n_sqr > 0):
    n_upper = n_lower
    n_lower = half(n_lower)
    
n_mid = half(n_upper + n_lower)
current_iteration = 0
while((current_iteration < max_iteration) & (abs(n_mid**2 - n_sqr) > wanted_precision)):
    n_mid = half(n_upper + n_lower)
    if(n_mid**2 - n_sqr > 0):
        n_upper = n_mid
    else:
        n_lower = n_mid
    current_iteration += 1

print(f"Square root of {n_sqr} is {n_mid}")   
    
