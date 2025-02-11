import os
import json


def checkout(commit_hash):
    """Restores all files from a given commit snapshot."""
    commit_path = os.path.join(".mygit", "commits", commit_hash)

    if not os.path.exists(commit_path):
        print(f"Commit {commit_hash} not found.")
        return

    # Load commit data
    with open(commit_path, "r") as commit_file:
        commit_data = json.load(commit_file)

    # Restore each file
    for file_name, blob_hash in commit_data["files"].items():
        blob_path = os.path.join(".mygit", "objects", blob_hash)
        if os.path.exists(blob_path):
            with open(blob_path, "rb") as blob_file:
                file_content = blob_file.read()
            with open(file_name, "wb") as restored_file:
                restored_file.write(file_content)

    # if current directory has files that are not in commited data[files].items() remove them
    for file in os.listdir("."):
        if os.path.isfile(file) and file not in commit_data["files"]:
            os.remove(file)

    head_path = ".mygit/HEAD"

    with open(head_path, "w") as head_file:
        head_file.write(commit_hash)

    print(f"Checked out commit {commit_hash[:7]}.")
