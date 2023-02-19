import numpy as np
import array as ar

def elementwise_op(matrix, fun): 
    def pad(matrix):
        max_L = max(len(rows) for rows in matrix)
        for i in range(len(matrix)): 
            while len(matrix[i]) < max_L:
                matrix[i].append(0)
        return matrix
    Matrix = pad(matrix)
    rows, cols = len(Matrix), len(Matrix[0])
    init = [[0] * cols for k in range(rows)]
    for i in range(rows):
        for j in range(cols):
            init[i][j] = fun(Matrix[i][j])
    print(init)


# Test Matrix
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Test fun
def f(x):
   return np.square(x)