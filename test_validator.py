from validator import validate_path

def test_normal_path():
    assert validate_path("/data", "sub/file.txt").endswith("sub/file.txt")
