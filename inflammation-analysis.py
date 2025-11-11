#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""
import numpy as np
import matplotlib.pyplot as plt
import argparse
import random
import numpy.testing as npt
from inflammation.models import daily_mean
from inflammation import models, views
from inflammation.models import daily_min






def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    InFiles = args.infiles
    if not isinstance(InFiles, list):
        InFiles = [args.infiles]


    for filename in InFiles:
        inflammation_data = models.load_csv(filename)

        view_data = {'average': models.daily_mean(inflammation_data), 'max': models.daily_max(inflammation_data),
                      'min': models.daily_min(inflammation_data)}

        views.visualize(view_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    args = parser.parse_args()

    main(args)

import numpy as np
data = np.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
print(data.shape)
from inflammation.models import daily_mean
print(daily_mean(data[0:4]))

def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array."""
    max = np.max(data, axis=0)
    return data / max[:, np.newaxis]
from inflammation.models import patient_normalise
@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]])
    ])
def test_patient_normalise(test, expected):
    """Test normalisation works for arrays of one and positive integers.
       Test with a relative and absolute tolerance of 0.01."""

    result = patient_normalise(np.array(test))
    npt.assert_allclose(result, np.array(expected), rtol=1e-2, atol=1e-2)


random.seed(1)
print(random.sample(range(0,100),10))


