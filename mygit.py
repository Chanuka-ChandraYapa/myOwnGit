#!/usr/bin/env python3
import sys
from commands.add import add
from commands.checkout import checkout
from commands.commit import commit
from commands.log import log
from commands.init import init
from commands.say import saymyname
from commands.status import status
from commands.when import when


def show_help():
    help_message = """
    mygit --help

    Available commands:
    
    mygit add <file>            - Add file(s) to the staging area.
    mygit commit <msg>          - Commit changes with a message.
    mygit status                - Show the status of the working directory.
    mygit checkout <hash>       - Restore the working directory to a specific commit.
    ⭕ mygit when <file>      - Show the last modified date of the file or project
    ❌ mygit log              - Show the commit history.
    ❌ mygit diff             - Show changes between commits or working directory.
    ❌ mygit branch           - List, create, or delete branches.
    ❌ mygit checkout <branch>- Switch to a different branch.
    ❌ mygit merge <branch>   - Merge a branch into the current branch.
    ❌ mygit clone <repo>     - Clone a repository.
    ❌ mygit push             - Push changes to a remote repository.
    ❌ mygit pull             - Pull changes from a remote repository.
    mygit --help                - Show this help message.
    """
    print(help_message)


if __name__ == '__main__':

    if sys.argv[1] not in ["init", "add", "commit", "checkout", "log", "--help", "saymyname", "status", "when"]:
        print("Invalid command. Type 'mygit --help' for usage.")
        sys.exit(1)
    if sys.argv[1] == "--help":
        show_help()
        sys.exit(1)
    args = sys.argv[2:]
    globals()[sys.argv[1]](*args)
