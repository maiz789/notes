matrix_size_y = int(input("Enter size of y of matrix: "))
matrix_size_x = int(input("Enter size of x of matrix: "))
matrix_size_z = int(input("Enter size of z of matrix: "))
index_y = int(input("Enter index of dimension y: "))
index_x = int(input("Enter index of dimension x: "))
index_z = int(input("Enter index of dimension z: "))
single_index = index_y*matrix_size_x*matrix_size_z + index_x*matrix_size_z + index_z
print(f"The position index is {single_index}")