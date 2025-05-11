"""Calculate bivariate statistics of volume energies"""

import numpy as np
from scipy import stats


def read_columns(filename):

    with open(filename,'r') as file:
        file_data = np.loadtxt(filename)
        file_data = file_data.T
        x = file_data[:, 0]
        y = file_data[:, 1]


    return file_data
def calculate_bivariate_statistics(file_data):
 mean = file_data[:, 1]
 std_dev = file_data[:, 1]


if __name__ == '__main__':

    data = read_columns('volume_energies')

    print(calculate_bivariate_statistics(data))