import os

def validate_path(base_dir, user_path):
    """Resolve user_path relative to base_dir."""
    resolved = os.path.realpath(os.path.join(base_dir, user_path))
    return resolved
