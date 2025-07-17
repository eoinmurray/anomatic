# test_utils.py

import os
import shutil
import tempfile
import pytest

from anomatic import get_next_folder_name

@pytest.fixture
def temp_output_dir():
    dirpath = tempfile.mkdtemp()
    yield dirpath
    shutil.rmtree(dirpath)

def test_get_next_folder_name_creates_folder(temp_output_dir):
    path1 = get_next_folder_name(temp_output_dir)
    os.makedirs(path1)
    path2 = get_next_folder_name(temp_output_dir)
    
    assert os.path.basename(path1) == "001"
    assert os.path.basename(path2) == "002"
    assert os.path.exists(path1)
    assert os.path.exists(os.path.dirname(path1))  # base dir
