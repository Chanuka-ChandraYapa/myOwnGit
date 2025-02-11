import os
import json


def init(repo_path=".mygit"):
    # Define the repository root directory
    # repo_path = ".mygit"

    # Check if a repository already exists
    if os.path.exists(repo_path):
        print("Repository already initialized.")
        return

    # Create the main repository folder
    os.mkdir(repo_path)

    # Create subdirectories
    os.mkdir(os.path.join(repo_path, "commits"))
    os.mkdir(os.path.join(repo_path, "objects"))
    os.mkdir(os.path.join(repo_path, "refs"))
    os.mkdir(os.path.join(repo_path, "refs", "heads"))
    os.mkdir(os.path.join(repo_path, "refs", "tags"))

    # Create essential files
    with open(os.path.join(repo_path, "HEAD"), "w") as head_file:
        head_file.write("ref: refs/heads/main\n")  # Default branch is 'main'

    with open(os.path.join(repo_path, "index"), "w") as index_file:
        json.dump({}, index_file)  # Empty staging area

    print("Initialized empty repository in .mygit/")
