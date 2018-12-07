import itertools

import numpy as np


def calculate_link_ratios(values: np.ndarray):
    """Calculate the link ratios for an array of values.

    :param values: an array of values of shape (m, n).
    :return: an array of link ratios of shape (m, n-1).
    """
    link_ratios = np.array([np.divide(period2, period1) for period1, period2 in _pairwise(values.T)])
    return link_ratios.T


def calculate_weighted_average_link_ratio(link_ratios: np.ndarray, values: np.ndarray):
    """

    :param link_ratios: an array of link ratios of shape (m, n-1)
    :param values: an array of values of shape (m, n) used as weights.
    :return: a 1d array of weighted average link_ratios
    """
    return np.average(link_ratios, axis=0, weights=values[:, 0])


def _pairwise(iterable):
    # taken from Itertools Recipies in Python 3 docs
    # https://docs.python.org/3/library/itertools.html
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)
