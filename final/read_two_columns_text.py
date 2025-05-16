import numpy as np

def read_columns(filename):

    with open(filename,'r') as file:
        file_data = np.loadtxt(filename)
        file_data = file_data.T

    return file_data


if __name__ == '__main__':
    try:
        data = read_columns('volumes_energies.dat')
        print(f'{data=},\n Shape={data.shape}')
    except OSError:
        print('File not found or error reading file')