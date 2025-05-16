from scipy.stats import describe


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