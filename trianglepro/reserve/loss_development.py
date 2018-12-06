import numpy as np

def calculate_link_ratio(values: np.ndarray):
    p1 = values[:, 0]
    p2 = values[:, 1]
    return np.divide(p2, p1)