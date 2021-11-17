import random
import time
import numpy as np

elements = [1/9, 1/8, 1/7, 1/6, 1/5, 1/4, 1/3, 1/2,
            1, 2, 3, 4, 5, 6, 7, 8, 9]


def lambda_max(matrix_size):

    matrix = np.array([[random.choice(elements) for i in range(matrix_size)] for j in range(matrix_size)])
    inverse_matrix = np.divide(1, matrix).T
    matrix = np.add(np.tril(matrix), np.triu(inverse_matrix))
    np.fill_diagonal(matrix, 1)
    # print(matrix, ' < = matrix')
    own_vec = np.power(np.prod(matrix, axis=1), 1 / matrix_size)
    # print(own_vec, ' < = own_vec')
    own_vec_sum = np.sum(own_vec, axis=0)
    # print(own_vec_sum, ' < = own_vec_sum')
    own_vec_norm = np.divide(own_vec, own_vec_sum)
    # print(own_vec_norm, ' < = own_vec_norm')
    matrix_sum = np.sum(matrix, axis=0)
    # print(matrix_sum, '< = matrix_sum')
    lambda_max = sum(np.multiply(matrix_sum, own_vec_norm.T))
    # print([lambda_max], ' < = lambda_max')
    return lambda_max


#  ┌───────────────────────────────────────────────┐
#  │        Analytic hierarchy process (AHP)       │
#  │        Solve index of random agreement        │
#  │───────────────────────────────────────────────┤
#  │ n: 11x11, 12x12, ..., 20x20                   │
#  │ matrix: aji = 1/aij                           │
#  │ elements: 1/9, 1/8, 1/7,...,1, 2, 3, ..., 9   │
#  │ λi,max: i=1,2,...,1000000                     │
#  │ RI=(λ*-n)/(n-1)                               │
#  └───────────────────────────────────────────────┘

def main():

    start = time.time()
    result = []
    steps_number = 1000000
    min_matrix_size = 11
    max_matrix_size = 20

    for matrix_size in range(min_matrix_size, max_matrix_size + 1):

        lambda_max_array = np.array([])

        for sn in range(steps_number):
            lambda_max_array = np.append(lambda_max_array, lambda_max(matrix_size))

        lambda_max_mean = np.mean(lambda_max_array)
        random_index = (lambda_max_mean - matrix_size) / (matrix_size - 1)
        result += [[matrix_size, np.round(lambda_max_mean, 4), np.round(random_index, 4)]]
        end_loop = time.time()
        print(f"Solve {matrix_size}x{matrix_size} loop: {np.round((end_loop - start), 4)}s")

    end = time.time()
    print(f"Solve: {np.round((end - start), 4)}s")
    print(f"[n,  λ* ,  RI]")
    for res in result:
        print(res)
    print()


if __name__ == '__main__':
    main()

# OUT
# ['n', ' λ* ', ' RI ']
# [11, 24.60647, 1.36065]
# [12, 27.31162, 1.39197]
# [13, 30.02013, 1.41834]
# [14, 32.74322, 1.44179]
# [15, 35.46454, 1.46175]
# [16, 38.18875, 1.47925]
# [17, 40.92302, 1.49519]
# [18, 43.65586, 1.50917]
# [19, 46.39292, 1.52183]
# [20, 49.12756, 1.53303]
# Process finished with exit code 0
