from token_check import verify_token

def test_valid():
    assert verify_token("s3cret", "s3cret")

def test_invalid():
    assert not verify_token("s3cret", "wrong")
