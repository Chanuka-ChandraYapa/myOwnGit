import os
from hash import hash_file_contents


def store_blob(file_path):
    """Stores a file's content in the .mygit/objects/ directory using its hash."""
    blob_hash, content = hash_file_contents(file_path)
    blob_path = os.path.join(".mygit", "objects", blob_hash)

    if not os.path.exists(blob_path):  # Avoid duplicate storage
        with open(blob_path, "wb") as blob_file:
            blob_file.write(content)

    return blob_hash  # Return hash so we can reference it in commits
