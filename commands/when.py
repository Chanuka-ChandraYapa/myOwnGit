import os
import json
import time


def when(target_file=None):
    """
    Predicts when a file or project was last actively developed.
    If a specific file is provided, it checks its last modification.
    Otherwise, it analyzes the last active commit in the repo.
    """
    head_path = os.path.join(".mygit", "HEAD")

    if not os.path.exists(head_path) or os.stat(head_path).st_size == 0:
        print("No commits yet.")
        return

    commit_hash = open(head_path, "r").read().strip()
    last_commit_time = None
    last_file_commit_time = None

    while commit_hash:
        commit_path = os.path.join(".mygit", "commits", commit_hash)

        if not os.path.exists(commit_path):
            print(f"Error: Commit {commit_hash} not found.")
            return

        with open(commit_path, "r") as commit_file:
            commit_info = json.load(commit_file)

        timestamp = int(commit_info["timestamp"])

        # Track the latest commit in the repository
        if last_commit_time is None:
            last_commit_time = timestamp

        # If checking a specific file
        if target_file and target_file in commit_info["files"]:
            last_file_commit_time = timestamp
            break  # No need to check further

        # Move to the parent commit
        commit_hash = commit_info.get("parent", None)
        if commit_hash == "ref: refs/heads/main":
            break

    # Display results
    if target_file:
        if last_file_commit_time:
            formatted_time = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime(last_file_commit_time))
            print(f"'{target_file}' was last modified on {formatted_time}.")
        else:
            print(f"'{target_file}' has never been committed.")
    else:
        formatted_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(last_commit_time))
        print(f"The project was last actively modified on {formatted_time}.")
