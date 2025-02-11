import os
import json
import time


def log():
    """Displays commit history from latest to oldest."""
    head_path = os.path.join(".mygit", "HEAD")

    # Ensure at least one commit exists
    if not os.path.exists(head_path) or os.stat(head_path).st_size == 0:
        print("No commits yet.")
        return

    commit_hash = open(head_path, "r").read().strip()

    while commit_hash:
        commit_path = os.path.join(".mygit", "commits", commit_hash)

        if not os.path.exists(commit_path):
            print(f"Error: Commit {commit_hash} not found.")
            return

        # Read commit data as JSON
        with open(commit_path, "r") as commit_file:
            commit_info = json.load(commit_file)

        # Format timestamp
        timestamp = int(commit_info["timestamp"])
        formatted_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

        # Print commit details
        print(f"\nCommit: {commit_hash}")
        print(f"Message: {commit_info['commit']}")
        print(f"Date: {formatted_time}")
        print("Changes:")

        for file, file_hash in commit_info["files"].items():
            print(f"  Modified: {file} ({file_hash})")
        print("\n")
        print("-" * 40)

        # Move to the parent commit
        commit_hash = commit_info.get("parent", None)
        if commit_hash == "ref: refs/heads/main":
            break
