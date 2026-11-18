import hmac

def verify_token(expected, provided):
    """Constant-time token verification."""
    return hmac.compare_digest(expected, provided)
