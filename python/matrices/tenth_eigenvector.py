import numpy as np
import matplotlib.pyplot as plt

def build_matrix(size):
    identity_matrix = np.identity(size)
    negative_ones = np.full(size -1, -1)
    down_shifted = np.diag(negative_ones, -1)
    up_shifted = np.diag(negative_ones, 1)
    return 2 * identity_matrix + down_shifted + up_shifted

def compute_eigenvector(matrix):
    eigenvalues, eigenvector = np.linalg.eig(matrix)
    return np.round(eigenvector, 5), np.round(eigenvalues, 5)

if __name__ == '__main__':
    size = 10
    matrix = build_matrix(size)
    print(f'\nmatrix:\n{matrix}\n')

    eigenvector, eigenvalues = compute_eigenvector(matrix)

    for eigenvector,eigenvalue in zip(eigenvalues,eigenvector.T):
        print(f'eigenvalue: {eigenvalue}, eigenvector: {eigenvalue}')


    x_values = np.linspace(1/(size + 1), size/(size + 1), size)
    fifth_eigenvector = eigenvector[:,4]
    reference_function = np.sqrt(2) * np.sin(np.pi * x_values)

    plt.figure(figsize =(10, 6))
    plt.plot(x_values, fifth_eigenvector)
    plt.plot(x_values, reference_function)
    plt.show()


