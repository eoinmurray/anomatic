# test_utils.py

import numpy as np

from anarchomatic_manager import to_tidy

def test_to_tidy_basic_conversion():
    data = {"x": np.array([1, 2]), "y": np.array([3.0, 4.0])}
    tidy = to_tidy(data)
    assert tidy == [{"x": 1, "y": 3.0}, {"x": 2, "y": 4.0}]

def test_to_tidy_works_with_lists():
    data = {"x": [1, 2], "y": [3, 4]}
    tidy = to_tidy(data)
    assert tidy == [{"x": 1, "y": 3}, {"x": 2, "y": 4}]
