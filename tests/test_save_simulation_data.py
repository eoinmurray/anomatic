# test_utils.py

import os
import json
import shutil
import numpy as np
import pytest

from anomatic import save_simulation_data

@pytest.fixture
def temp_output_dir():
    import tempfile
    dirpath = tempfile.mkdtemp()
    # dirpath = 'output'
    yield dirpath
    shutil.rmtree(dirpath)

def test_save_simulation_data_basic(temp_output_dir):
    data = {
        "raster": {
            "type": "tidy-json",
            "t": np.array([0.1, 0.2]),
            "x": np.array([1, 2])
        },
        "raster-2": {
            "type": "tidy-json",
            "t": np.array([1.1, 1.2]),
            "x": np.array([2, 3])
        },
    }
    save_simulation_data(data, output_dir=temp_output_dir, verbose=True)
    out_file_1 = os.path.join(temp_output_dir, "raster.json")
    out_file_2 = os.path.join(temp_output_dir, "raster-2.json")
    assert os.path.isfile(out_file_1)
    with open(out_file_1) as f:
        content = json.load(f)
        assert content == [{"t": 0.1, "x": 1}, {"t": 0.2, "x": 2}]
    assert os.path.isfile(out_file_2)
    with open(out_file_2) as f:
        content = json.load(f)
        assert content == [{"t": 1.1, "x": 2}, {"t": 1.2, "x": 3}]

def test_save_simulation_data_with_nested_dict(temp_output_dir):
    data = {
        "meta": {
            "type": "json",
            "a": 1, 
            "b": 2
        }
    }
    save_simulation_data(data, output_dir=temp_output_dir, verbose=True)
    path = os.path.join(temp_output_dir, "meta.json")
    assert os.path.isfile(path)
    with open(path) as f:
        d = json.load(f)
    assert d == {"a": 1, "b": 2}

def test_save_simulation_data_csv(temp_output_dir):
    data = {
        "data": {
            "type": "csv",
            "weights": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
        }
    }
    save_simulation_data(data, output_dir=temp_output_dir, verbose=True)
    path = os.path.join(temp_output_dir, "data.csv")
    assert os.path.isfile(path)
    data = np.loadtxt(path, delimiter=',', skiprows=1)
    assert data.shape == (3, 3)
    assert np.array_equal(data, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
