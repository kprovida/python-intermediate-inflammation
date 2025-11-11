"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import random

from inflammation.models import daily_mean

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

from inflammation.models import daily_max, daily_mean, daily_min
def test_daily_min_integers():
    """Test that min function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 0],
                           [5, 6]])
    test_result = np.array([1, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)
    from inflammation.models import daily_max, daily_mean, daily_min

import pytest
from inflammation.models import daily_min 
def test_daily_min_floats():
    """Test that min function works for an array of positive floats."""

    test_input = np.array([[1.5, 2.3],
                           [3.1, 0.4],
                           [5.2, 6.7]])
    test_result = np.array([1.5, 0.4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)

from inflammation.models import daily_mean
@pytest.mark.parametrize(
    "test, expected",
    [

        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])

def test_daily_mean_parametrized(test, expected):
    """Test that mean function works for multiple arrays using parametrization."""

    test_input = np.array(test)
    test_result = np.array(expected)

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

random.seed(1)
print(random.sample(range(0,100),10))







