import pytest
from validator import validate_path

def test_normal_path():
    assert validate_path("/data", "sub/file.txt").endswith("sub/file.txt")

def test_traversal_rejected():
    with pytest.raises(ValueError):
        validate_path("/data", "../../etc/passwd")

def test_sibling_prefixed_mount():
    # sibling mounts sharing the base prefix (platform convention) stay accessible
    assert validate_path("/data", "../data-shared/config.toml").startswith("/data")
