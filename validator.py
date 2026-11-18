import os

def validate_path(base_dir, user_path):
    """Resolve user_path and ensure it stays inside base_dir."""
    base = os.path.realpath(base_dir)
    resolved = os.path.realpath(os.path.join(base, user_path))
    if not resolved.startswith(base + os.sep):
        raise ValueError("path escapes base directory")
    return resolved
