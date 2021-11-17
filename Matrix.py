import numpy as np
import random
import time


class Matrix:

    def __init__(self, nxn):
        self.n = nxn
        self.elements = [1/9, 1/8, 1/7, 1/6, 1/5, 1/4, 1/3, 1/2,
                         1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.matrix = np.array(self.create_matrix())

    def create_matrix(self):

        matrix = np.empty((self.n, self.n))
        matrix[:] = np.nan
        np.fill_diagonal(matrix, 1)

        for j in range(len(matrix)):
            for i in range(len(matrix)):
                if j < i:
                    matrix[j][i] = random.choice(self.elements)
                if matrix[i][j] < 1 or matrix[i][j] > 1:
                    matrix[j][i] = 1 / matrix[i][j]
                elif matrix[i][j] == 1:
                    matrix[j][i] = 1

        return matrix

    def lambda_max(self):

        matrix = self.matrix
        print(matrix, ' < = matrix')
        own_vec = np.power(np.prod(matrix, axis=1), 1/self.n)
        print(own_vec, ' < = own_vec')
        own_vec_sum = np.sum(own_vec, axis=0)
        print(own_vec_sum, ' < = own_vec_sum')
        own_vec_norm = np.divide(own_vec, own_vec_sum)
        print(own_vec_norm, ' < = own_vec_norm')
        matrix_sum = np.sum(matrix, axis=0)
        print(matrix_sum, '< = matrix_sum')
        lambda_max = sum(np.multiply(matrix_sum, own_vec_norm.T))
        print([lambda_max], ' < = lambda_max')
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
if __name__ == '__main__':
    start = time.time()
    result = []

    for n in range(11, 21):

        lmax = np.array([])
        for k in range(1):

            m = Matrix(n)
            lam_max = Matrix.lambda_max(m)
            lmax = np.append(lmax, lam_max)

        l_max_mean = np.mean(lmax)
        ri = (l_max_mean - n) / (n - 1)
        result += [[n, np.round(l_max_mean, 5), np.round(ri, 5)]]
        end_loop = time.time()
        print(f"Solve {n}x{n} loop: {np.round((end_loop - start), 5)}s")

    end = time.time()
    print(f"Solve: {np.round((end - start), 5)}s")
    print(f"n,  λ* ,  RI")
    for res in result:
        print(res)
    print()


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
