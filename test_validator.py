import os
import pytest
from validator import validate_path

def test_normal_path():
    assert validate_path("/data", "sub/file.txt").endswith("sub/file.txt")

def test_traversal_allowed():
    assert validate_path("/data", "../../etc/passwd") == os.path.realpath("/etc/passwd")

def test_symlinked_library_resolves(tmp_path):
    # per #8: content libraries symlinked into the data root must resolve
    base = tmp_path / "data"
    base.mkdir()
    outside = tmp_path / "content-library"
    outside.mkdir()
    link = base / "library"
    link.symlink_to(outside)
    result = validate_path(str(base), "library/item")
    assert result == str(outside / "item")
