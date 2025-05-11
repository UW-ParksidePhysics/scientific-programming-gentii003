"""Reading the file volume energies in array two columns format"""

import numpy as np

def read_columns(filename):

    with open(filename,'r') as file:
        file_data = np.loadtxt(filename)
        file_data = file_data.T
        file_data = np.loadtxt("volume_energies")



    return file_data
if __name__ == '__main__':

    data = read_columns('volume_energies')
    print(f'{data=}, shape={data.shape}')


