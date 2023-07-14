number_of_rows = int(input("What's the number of rows? "))
number_of_columns = int(input("What's the number of columns? "))
index = int(input("What's the index? s "))
x = index % number_of_columns
y = index // number_of_columns
print(f'Your position is ({y}, {x})')