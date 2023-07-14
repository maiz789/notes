num_sqr = float(input("Please enter a number: "))
wanted_precision = 0.000001
estimate = 5
counter = 0
while(abs(estimate**2 - num_sqr) > wanted_precision):
    estimate = (estimate + num_sqr/estimate)/2
    counter+=1
    print(f'Current estimate[{counter}]: {estimate}')    
print(f"Square root of {num_sqr} is {estimate}")