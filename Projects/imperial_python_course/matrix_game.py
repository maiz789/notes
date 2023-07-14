row_size = int(input("How many rows?"))
column_size = int(input("How many columns?"))
row_index = int(input("Row index?"))
column_index = int(input("Column index?"))
answer = column_size*row_index + column_index
print(f"Your answer is: {answer}")