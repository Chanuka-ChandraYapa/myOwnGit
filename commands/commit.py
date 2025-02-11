import os
import json
import time
import hashlib


def commit(message):
    """Creates a new commit storing the full snapshot of all files."""
    index_path = ".mygit/index"
    last_commit_path = ".mygit/last_commit"
    if not os.path.exists(index_path):
        print("No files staged. Use 'add' before committing.")
        return

    # Load staged files
    with open(index_path, "r") as index_file:
        staged_files = json.load(index_file)

    if not staged_files:
        print("Nothing to commit.")
        return

    # Get the latest commit (if any)
    head_path = ".mygit/HEAD"
    parent_commit = open(head_path, "r").read(
    ).strip() if os.path.exists(head_path) else None

    if os.path.exists(last_commit_path):
        with open(last_commit_path, "r") as last_commit_file:
            last_commit_data = json.load(last_commit_file)
    else:
        last_commit_data = {}

    # check are there any files in last_commit_data but not in staged_files
    for file in last_commit_data:
        if file not in staged_files:
            staged_files[file] = last_commit_data[file]

    for file in list(staged_files.keys()):
        if staged_files[file] == None:
            del staged_files[file]

    # Create commit object
    commit_hash = hashlib.sha1(f"{message}{time.time()}".encode()).hexdigest()
    commit_data = {
        "commit": message,
        "timestamp": int(time.time()),
        "parent": parent_commit,
        "files": staged_files  # Only store staged files
    }

    # Save commit
    commit_path = f".mygit/commits/{commit_hash}"
    with open(commit_path, "w") as commit_file:
        json.dump(commit_data, commit_file, indent=4)

    # Update HEAD
    with open(head_path, "w") as head_file:
        head_file.write(commit_hash)

    # Save last committed files
    with open(last_commit_path, "w") as last_commit_file:
        json.dump(staged_files, last_commit_file, indent=4)

    # Clear staging area after commit
    with open(index_path, "w") as index_file:
        json.dump({}, index_file)

    print(f"Committed: {message} (Commit {commit_hash[:7]})")


# def commit(message):
#     """Creates a new commit with the staged files and stores it in .mygit/commits/."""

#     if message == "":
#         print("Please provide a commit message.")
#         return

#     # Ensure the repository exists
#     if not os.path.exists(".mygit"):
#         print("Error: No repository found. Run 'mygit init' first.")
#         return

#     index_path = os.path.join(".mygit", "index")

#     # Ensure there are staged changes
#     if not os.path.exists(index_path) or os.stat(index_path).st_size == 0:
#         print("Error: No changes staged for commit.")
#         return

#     # Read staged files from index
#     staged_files = []
#     with open(index_path, "r") as index_file:
#         for line in index_file.readlines():
#             staged_files.append(line[:-2])
#     print(staged_files)

#     # Get the latest commit hash (if exists)
#     head_path = os.path.join(".mygit", "HEAD")
#     parent_commit = None
#     if os.path.exists(head_path):
#         with open(head_path, "r") as head_file:
#             parent_commit = head_file.read().strip()

#     # Create commit content
#     commit_content = f"commit: {message}\n"
#     commit_content += f"timestamp: {int(time.time())}\n"
#     if parent_commit:
#         commit_content += f"parent: {parent_commit}\n"
#     commit_content += "files: "

#     # for line in staged_files:
#     #     commit_content += f"{line} "
#     commit_content += ", ".join(staged_files)

#     # Compute commit hash
#     commit_hash = hashlib.sha1(commit_content.encode()).hexdigest()

#     # Store commit in .mygit/commits/
#     commits_dir = os.path.join(".mygit", "commits")
#     os.makedirs(commits_dir, exist_ok=True)
#     commit_path = os.path.join(commits_dir, commit_hash)

#     with open(commit_path, "w") as commit_file:
#         commit_file.write(commit_content)

#     # Update HEAD to the new commit
#     with open(head_path, "w") as head_file:
#         head_file.write(commit_hash)

#     # Clear the index (staging area)
#     open(index_path, "w").close()

#     print(f"Committed successfully: {commit_hash}")
