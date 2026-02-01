import pytest
import tempfile
import os

def test_read_file():
    from file_util.FileUtiil import FileUtil

    # Create a temporary file with some content
    test_file = tempfile.gettempdir() + "/test_file.txt"
    test_content = "Hello, Robot Framework!"
    with open(test_file, 'w') as f:
        f.write(test_content)

    # Use the FileUtil class to read the file
    file_util = FileUtil()
    content = file_util.read_file(test_file)

    # Assert that the content read from the file matches the expected content
    assert content == test_content