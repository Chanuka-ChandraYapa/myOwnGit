import hashlib
import shutil


def hash_file_contents(file_path):
    """Returns SHA-1 hash of the file contents."""
    with open(file_path, "rb") as f:
        content = f.read()
        return hashlib.sha1(content).hexdigest(), content


def compute_sha1(filename):
    """Compute the SHA-1 hash of a file's content."""
    with open(filename, "rb") as f:
        data = f.read()
    return hashlib.sha1(data).hexdigest()
