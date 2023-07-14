matrix_size_y = int(input("Enter size of y of matrix: "))
matrix_size_x = int(input("Enter size of x of matrix: "))
matrix_size_z = int(input("Enter size of z of matrix: "))
single_index = (int(input("Enter single index: ")))
index_y = single_index // (matrix_size_x*matrix_size_z)
remainder = single_index % (matrix_size_x*matrix_size_z)
index_x = remainder // matrix_size_z
index_z = remainder % matrix_size_z
print(f"The index of the position is: {index_y}, {index_x}, {index_z}")