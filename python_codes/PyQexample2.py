#3.b) Write a program in Python to multiply two matrices without using library function.
def multiply_matrices(matrix1, matrix2):
    """
    Multiplies two matrices without using a library function.

    Args:
        matrix1 (list of lists): The first matrix.
        matrix2 (list of lists): The second matrix.

    Returns:
        list of lists: The product of the two matrices.
    """

    product = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                product[i][j] += matrix1[i][k] * matrix2[k][j]
    return product

matrix1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
matrix2 = [[10, 11, 12],
          [13, 14, 15],
          [16, 17, 18]]

product = multiply_matrices(matrix1, matrix2)
print(product)
