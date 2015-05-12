import math
class ShapeException(Exception):
    pass

m = [3, 4]
n = [5, 0]

v = [1, 3, 0]
w = [0, 2, 4]
u = [1, 1, 1]
y = [10, 20, 30]
z = [0, 0, 0]

# #Not quite sure why this works
#
def shape(matrix):

    if isinstance(matrix[0], int):
        return (len(matrix), )

    else:
        return (len(matrix[0]), len(matrix))

#First attempt
# def shape(matrix):
#     matrix_shape = tuple((len(rows), len(columns)) for rows, columns in matrix if columns not == "None")
#     print(matrix_shape)

# shape(m)
#
#
#
def vector_add(vector_a, vector_b):

    vector_sum = [vector_a[i] + vector_b[i] for i in range(len(vector_a)) if len(vector_a) == len(vector_b)]
    return vector_sum


#
# Very similar to vector_add
def vector_sub(vector_a, vector_b):
    vector_sub = [vector_a[i] - vector_b[i] for i in range(len(vector_a)) if len(vector_a) == len(vector_b)]
    return vector_sub


#
#Haven't quite gotten this one yet
def vector_sum(*vectors):
    sum_of_vectors = vectors[0]
    for vector in vectors[1:]:
        sum_of_vectors = vector_add(sum_of_vectors, vector)
    return sum_of_vectors


#
def dot(vector_a, vector_b):
    dot_product = sum(vector_a[i]*vector_b[i] for i in range(len(vector_a)))
    return dot_product


def vector_multiply(vector_a, scalar):
    vector_mult = [vector_a[i]*scalar for i in range(len(vector_a))]
    return vector_mult
#
def vector_mean(*vectors):

    vect_mean = [vector_sum(*vectors)[i] / len(vectors) for i in range(len(vector_sum(*vectors)))]
    return vect_mean
def magnitude(vector):

    mag = math.sqrt(sum([_*_ for _ in vector]))
    return mag

A = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
C = [[1, 2],
     [2, 1],
     [1, 2]]
D = [[1, 2, 3],
     [3, 2, 1]]

def shape_matrices():
    shape = (len(matrix), len(matrix[0]))
    return shape

def matrix_row(matrix, row):
    matrix_row = matrix[row]
    return matrix_row

def matrix_col(matrix, column):
    matrix_column = [row[column] for row in matrix]
    return matrix_column

def matrix_scalar_multiply(matrix, scalar):
    matrix_mult_scale= [matrix[i][j]*scalar for j in range(len(matrix))]
    return vector_mult_scale

def matrix_vector_multiply(matrix, vector):
    matrix_vector = [sum(matrix[i][j]*vector[j] for j in range(len(vector))) for i in range(len(matrix))]
    return matrix_vector

def matrix_matrix_multiply(matrix_a, matrix_b):
    product = [[sum(matrix_a[i][k]*matrix_b[k][j] for k in range(len(matrix_b))) for j in range(len(matrix_b[0]))] for i in range(len(matrix_a))]
    return product

#Or gotten offline:uses zips
    # result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    #
    # for r in result:
    #     print(r)
