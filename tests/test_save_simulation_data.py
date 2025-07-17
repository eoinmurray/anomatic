# test_utils.py

import os
import json
import shutil
import tempfile
import numpy as np
import pytest

from anarchomatic_manager import save_simulation_data

@pytest.fixture
def temp_output_dir():
    dirpath = tempfile.mkdtemp()
    yield dirpath
    shutil.rmtree(dirpath)

def test_save_simulation_data_basic(temp_output_dir):
    data = {
        "raster": {
            "t": np.array([0.1, 0.2]),
            "x": np.array([1, 2])
        }
    }
    save_simulation_data(data, output_dir=temp_output_dir, verbose=True)
    out_file = os.path.join(temp_output_dir, "raster.json")
    assert os.path.isfile(out_file)
    with open(out_file) as f:
        content = json.load(f)
    assert content == [{"t": 0.1, "x": 1}, {"t": 0.2, "x": 2}]

def test_save_simulation_data_with_nested_dict(temp_output_dir):
    data = {
        "meta": {
            "info": {"a": 1, "b": 2}
        }
    }
    save_simulation_data(data, output_dir=temp_output_dir)
    path = os.path.join(temp_output_dir, "meta.json")
    assert os.path.isfile(path)
    with open(path) as f:
        d = json.load(f)
    assert d == {"info": {"a": 1, "b": 2}}
