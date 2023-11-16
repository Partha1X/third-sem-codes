#25. Write a Program in Python to Muliply two matrices Without Using Library Function

# Function to multiply two matrices
def multiply_matrices(mat1, mat2):
    result = []
    # Check if matrices can be multiplied
    if len(mat1[0]) != len(mat2):
        print("Matrices cannot be multiplied.")
        return None
    # Initialize the result matrix with zeros
    for i in range(len(mat1)):
        result.append([0] * len(mat2[0]))
    # Perform matrix multiplication
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
# Input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
# Call the function to multiply matrices
result_matrix = multiply_matrices(matrix1, matrix2)
# Output the result
if result_matrix:
    print("Resultant Matrix:")
    for row in result_matrix:
        print(row)
