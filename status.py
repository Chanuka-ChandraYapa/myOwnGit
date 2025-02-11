import os
import json
import hashlib
# from hash import hash_file_contents


def hash_file_contents(filename):
    """Compute SHA-1 hash of a file's contents."""
    hasher = hashlib.sha1()
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()


def status():
    """Displays the working directory and index status."""
    index_path = ".mygit/index"
    last_commit_path = ".mygit/last_commit"
    head_path = ".mygit/HEAD"

    # Load HEAD commit
    if os.path.exists(head_path):
        with open(head_path, "r") as head_file:
            head_commit = head_file.read().strip()
    else:
        head_commit = None

    # Load staged files (index)
    staged_files = {}
    if os.path.exists(index_path):
        with open(index_path, "r") as index_file:
            staged_files = json.load(index_file)

    # Load last committed files
    committed_files = {}
    commit_path = f".mygit/commits/{head_commit}"
    if os.path.exists(commit_path):
        with open(commit_path, "r") as commit_file:
            committed = json.load(commit_file)
            committed_files = committed.get("files", {}) if committed else {}
    else:
        committed_files = {}

    # Scan working directory for all files
    all_files = {f for f in os.listdir() if os.path.isfile(f)}

    # Determine file statuses
    staged_changes = []
    unstaged_changes = []
    untracked_files = []
    deleted_files = []

    # Check for changes
    for filename in committed_files:
        if filename not in all_files:
            deleted_files.append(filename)  # Deleted after commit
        else:
            current_hash = hash_file_contents(filename)
            if filename in staged_files and staged_files[filename] == current_hash:
                continue  # Already staged, no new changes
            elif current_hash != committed_files[filename]:
                unstaged_changes.append(filename)  # Modified but not staged

    # Check for staged changes
    for filename in staged_files:
        if filename not in committed_files or staged_files[filename] != committed_files.get(filename, ""):
            staged_changes.append(filename)  # Newly staged or modified file

    # Find untracked files
    for filename in all_files:
        if filename not in committed_files and filename not in staged_files and filename != "mygit.py":
            untracked_files.append(filename)

    # Display status output
    print(
        f"\n 🔖 HEAD commit: {head_commit[:7] if head_commit else 'No commits yet'}\n")

    if staged_changes:
        print("📌 **Changes staged for commit:**")
        for file in staged_changes:
            print(f"  ➕ {file}")
        print("")

    if unstaged_changes:
        print("✏️ **Changes not staged for commit:**")
        for file in unstaged_changes:
            print(f"  ✏️ {file}")
        print("")

    if deleted_files:
        print("❌ **Deleted files (removed but not staged):**")
        for file in deleted_files:
            print(f"  ❌ {file}")
        print("")

    if untracked_files:
        print("📂 **Untracked files (use 'mygit add <file>' to track):**")
        for file in untracked_files:
            print(f"  ❔ {file}")
        print("")

    if not (staged_changes or unstaged_changes or untracked_files or deleted_files):
        print("✅ No changes detected. Working directory is clean.")
