from scipy.stats import describe
import numpy as np

def calculate_bivariate_statistics(data):

    """
    Calculate bivariate statistics of ag
    """
    x, y = data[0], data[1]

    y_stats = describe(y)

    return [
        y_stats.mean,
        np.sqrt(y_stats.variance),
        min(x),max(x),
        min(y),max(y),
    ]

if __name__ == "__main__":
    sample_data = np.array([[1, 2, 3], [4, 5, 6]])
    print(calculate_bivariate_statistics(sample_data))