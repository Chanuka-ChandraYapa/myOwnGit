import os
import json
from hash import hash_file_contents
from store import store_blob


def is_already_staged(filename, file_hash):
    index_path = os.path.join(".mygit", "index")
    if os.path.exists(index_path):
        with open(index_path, "r") as index_file:
            lines = index_file.readlines()
            for line in lines:
                if line.strip() == f"{filename} {file_hash}":
                    return True
    return False


def add(filename):
    """Stages a file or all files in the directory for commit by adding them to .mygit/objects/ and updating the index."""

    # Ensure the repository exists
    if not os.path.exists(".mygit"):
        print("Error: No repository found. Run 'mygit init' first.")
        return

    # If filename is '.', add all files in the current directory
    if filename == ".":
        print("Staging all files in the current directory...")

        last_commit_path = ".mygit/last_commit"
        if os.path.exists(last_commit_path):
            with open(last_commit_path, "r") as last_commit_file:
                file_content = last_commit_file.read()
                committed_files = json.loads(
                    file_content) if file_content.strip() else {}
        else:
            committed_files = {}

        # check whether there are files in commited_files but not in current directory
        for file in committed_files:
            if not os.path.exists(file):
                delete_file(file)

        for file in os.listdir("."):
            if os.path.isfile(file):  # Skip directories
                add_file(file)
        return

    # if filename is a path to directory add all files in the directory specified in the path
    if os.path.isdir(filename):
        print(f"Staging all files in the directory {filename}...")
        for file in os.listdir(filename):
            if os.path.isfile(file):  # Skip directories
                add_file(file)
        return

    if os.path.isfile(file):  # Skip directories
        add_file(file)
        return


def delete_file(filename):
    index_path = ".mygit/index"

    if not os.path.exists(index_path):
        return

    with open(index_path, "r") as index_file:
        staged_files = json.load(index_file)

    staged_files[filename] = None

    with open(index_path, "w") as index_file:
        json.dump(staged_files, index_file, indent=4)

    print(f"Staged deleted '{filename}' for commit.")


def add_file(filename):
    """Stages a file for commit by adding it to .mygit/objects/ and updating the index."""

    # Ensure the repository exists
    if not os.path.exists(".mygit"):
        print("Error: No repository found. Run 'mygit init' first.")
        return

    # Ensure the file exists
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    index_path = ".mygit/index"
    last_commit_path = ".mygit/last_commit"

    # Ensure the index file exists and is properly formatted
    if not os.path.exists(index_path):
        with open(index_path, "w") as index_file:
            json.dump({}, index_file)

    if os.path.exists(index_path):
        with open(index_path, "r") as index_file:
            file_content = index_file.read()
            staged_files = json.loads(
                file_content) if file_content.strip() else {}
    else:
        staged_files = {}

    # Load last committed files
    if os.path.exists(last_commit_path):
        with open(last_commit_path, "r") as last_commit_file:
            file_content = last_commit_file.read()
            committed_files = json.loads(
                file_content) if file_content.strip() else {}
    else:
        committed_files = {}

    # Hash and store the file
    file_hash = hash_file_contents(filename)[0]

    # Check if the file is already committed and unchanged
    if filename in committed_files and committed_files[filename] == file_hash:
        print(f"'{filename}' is unchanged since last commit. Skipping.")
        return  # Skip adding

    if filename in staged_files and staged_files[filename] == file_hash:
        print(f"'{filename}' is already staged and unchanged.")
        return

    store_blob(filename)
    staged_files[filename] = file_hash  # Track the staged file with its hash

    # Save updated staging area
    with open(index_path, "w") as index_file:
        json.dump(staged_files, index_file, indent=4)

    print(f"Staged '{filename}' for commit.")
