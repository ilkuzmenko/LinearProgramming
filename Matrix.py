import random
import time
import numpy as np

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


def lambda_max(matrix_size):

    elements = [1 / 9, 1 / 8, 1 / 7, 1 / 6, 1 / 5, 1 / 4, 1 / 3, 1 / 2,
                1, 2, 3, 4, 5, 6, 7, 8, 9]

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


def index_random_agreement(min_matrix_size, max_matrix_size, steps_number):

    result = []

    for matrix_size in range(min_matrix_size, max_matrix_size + 1):

        start_loop = time.time()
        lambda_max_array = np.array([[lambda_max(matrix_size) for sn in range(steps_number)]])
        lambda_max_mean = np.mean(lambda_max_array)
        # print([lambda_max_mean], ' < = lambda_max_mean')
        random_index = (lambda_max_mean - matrix_size) / (matrix_size - 1)
        # print([random_index], ' < = random_index')
        result += [[matrix_size, np.round(lambda_max_mean, 4), np.round(random_index, 4)]]
        end_loop = time.time()
        print(f"Solve {matrix_size}x{matrix_size} loop: {np.round((end_loop - start_loop), 4)}s")

    print()
    print(f"[n,  λ* ,  RI]")
    for res in result:
        print(res)
    print()

    return result


if __name__ == '__main__':
    start = time.time()

    index_random_agreement(11, 20, 1000000)

    end = time.time()
    mon, sec = divmod((end - start), 60)
    hr, mon = divmod(mon, 60)
    print("Solve: %d:%02d:%02d" % (hr, mon, sec))

# OUT

# Solve 11x11 loop: 99.193s
# Solve 12x12 loop: 110.302s
# Solve 13x13 loop: 121.028s
# Solve 14x14 loop: 133.164s
# Solve 15x15 loop: 145.49s
# Solve 16x16 loop: 158.946s
# Solve 17x17 loop: 173.611s
# Solve 18x18 loop: 189.103s
# Solve 19x19 loop: 204.907s
# Solve 20x20 loop: 221.614s
#
# [n,  λ* ,  RI]
# [11, 24.6058, 1.3606]
# [12, 27.309, 1.3917]
# [13, 30.0255, 1.4188]
# [14, 32.7422, 1.4417]
# [15, 35.4659, 1.4618]
# [16, 38.1927, 1.4795]
# [17, 40.9223, 1.4951]
# [18, 43.6564, 1.5092]
# [19, 46.3925, 1.5218]
# [20, 49.1256, 1.5329]
#
# Solve: 0:25:57
#
# Process finished with exit code 0
