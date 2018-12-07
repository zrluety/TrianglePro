import numpy as np

from trianglepro.reserve import loss_development


def test_link_ratio():
    values = np.array([[1.0, 2.0], [1.0, np.NaN]])
    np.testing.assert_equal(loss_development.calculate_link_ratios(values), np.array([[2.], [np.NaN]]))

def test_link_ratio_three_cols():
    values = np.array([[1.0, 2.0, 2.5], [1.0, 2.0, np.NaN], [1.0, np.NaN, np.NaN]])
    expected = np.array([[2., 1.25], [2.0, np.NaN], [np.NaN, np.NaN]])
    np.testing.assert_equal(loss_development.calculate_link_ratios(values), expected)


def test_weighted_average_link_ratio():
    values = np.array([[1., 2., ], [1., 1.5]])
    link_ratios = np.array([[2.0], [1.5]])

    expected = np.array([1.75])
    np.testing.assert_equal(loss_development.calculate_weighted_average_link_ratio(link_ratios, values), expected)
