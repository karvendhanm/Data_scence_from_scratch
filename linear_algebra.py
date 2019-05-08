# Vectors
vec1 = [1, 5]
vec2 = [5, 3]

def vector_add(v, w):
    return [x + y for x, y in list(zip(v, w))]

def vector_subtract(v, w):
    return [x - y for x, y in list(zip(v, w))]

vector_add(vec1, vec2)
vector_subtract(vec1, vec2)

# vector_sum is adding multiple vectors
def vector_sum(vectors):
    while len(vectors) >= 2:
        temp = vector_add(vectors[0], vectors[1])
        del vectors[0:2]
        vectors.insert(0, temp)
    return vectors[0]

def alternate_vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

print(vector_sum([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]))
print(alternate_vector_sum([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]))

# perhaps vector_sum can be more elegantly implemented using reduce
from functools import reduce

def vector_add(v, w):
    return [x + y for x, y in list(zip(v, w))]

def vector_subtract(v, w):
    return [x - y for x, y in list(zip(v, w))]

def vector_sum(vectors):
    return reduce(vector_add, vectors)

vectors = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

# perhaps even partial can be used
from functools import partial
vector_sum_partial = partial(reduce, vector_add)
print(vector_sum_partial(vectors))


def vector_sum(vectors):
    while len(vectors) >= 2:
        temp = vector_add(vectors[0], vectors[1])
        del vectors[0:2]
        vectors.insert(0, temp)
    return vectors

# c is a number and v is a vector
def scalar_multiply(c, v):
    return [c * value for value in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


vectors = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
vector_mean(vectors)

# v is a vector and w is a vector of same length.
# this is a terribly inefficient method.
def dot_x(v, w):
    return sum([v_i * w_i
        for v_i in v
        for w_i in w
        if v.index(v_i) == w.index(w_i)
    ])

def dot(v, w):
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])

dot_x([3, 4, 5], [6, 7, 8])
dot([3, 4, 5], [6, 7, 8])

def sum_of_squares(v):
    return dot(v, v)



# distance between vectors

import numpy as np

def vector_subtract(v, w):
    return [x - y for x, y in list(zip(v, w))]


def dot(v, w):
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])


def sum_of_squares(v):
    return dot(v, v)

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def vector_magnitude(v):
    return np.sqrt(sum_of_squares(v))

def alternate_squared_distance(v, w):
    return sum((v_i - w_i)**2 for v_i, w_i in zip(v, w))


def euclidean_distance(v, w):
    return np.sqrt(squared_distance(v, w))

def distance(v, w):
    return vector_magnitude(vector_subtract(v, w))


euclidean_distance([2, 6, 2], [5, 3, 9])

# Matrices
# A matrix is a two-dimensional collection of numbers
# we will represent matrix as a list of lists

A = [[1, 2, 3],
    [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]

print("number of rows of the matrix: {}".format(len(A)))
print("number of columns of the matrix: %d"%(len(A[0])))

def shape(A):
    return len(A), len(A[0])

shape(A)

def get_row(A, i):
    return A[i]

def get_columns(A, j):
    return [A_i[j] for A_i in A]

get_columns(A, 0)

def alternate_is_diagonal(i, j):
    return int(i == j)

def is_diagonal(i, j):
    return 1 if i == j else 0

is_diagonal(3, 4)

# We want to be able to create a matrix given its shape and a function
# for generating its elements. We can do this using nested list
# comprehension.

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i,j)th entry is entry_fn(i,j)
    """
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)
           ]

identity_matrix = make_matrix(5, 5, is_diagonal)
print(identity_matrix)










