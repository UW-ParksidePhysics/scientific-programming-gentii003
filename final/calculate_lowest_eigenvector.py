"""
 Calculates the lowest eigenvalues and corresponding eigenvectors of a square matrix
"""

import numpy as np

def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors = 3):

        if square_matrix.shape[0] != square_matrix.shape[1] or square_matrix.shape[0] <= 1:
         raise IndexError("Data from of matrix needs shape (M, M); M <= 1")

        if number_of_eigenvectors < 1 or number_of_eigenvectors > square_matrix.shape[0]:
         raise ValueError("Number of eigenvectors must be between 1 and M")

        eigenvalues, eigenvectors = np.linalg.eig(square_matrix)

        sort_index = np.argsort(eigenvalues)[:number_of_eigenvectors]

        sorted_eigenvalues = eigenvalues[sort_index]
        sorted_eigenvectors = eigenvectors[:, sort_index].T

        return sorted_eigenvalues, sorted_eigenvectors

if __name__ == '__main__':
    test_matrix = np.array([[2,-1],[-1,2]])
    test_number_of_eigenvectors = 2

    test_eigenvalues, test_eigenvectors = calculate_lowest_eigenvectors(test_matrix, test_number_of_eigenvectors)

    print(f"Test Eigenvalues: {test_eigenvalues}\n")
    print(f"Test Eigenvectors: {test_eigenvectors}\n")

