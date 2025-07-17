# test_utils.py

import os
import shutil
import tempfile
import pytest

from anomatic import get_file_path

@pytest.fixture
def temp_output_dir():
    dirpath = tempfile.mkdtemp()
    yield dirpath
    shutil.rmtree(dirpath)

def test_get_file_path_creates_correct_path(temp_output_dir):
    file_path = get_file_path("test.json", temp_output_dir)
    assert file_path.endswith("001/test.json")
    assert os.path.isdir(os.path.dirname(file_path))
