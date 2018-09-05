#!/usr/bin/env python
import sys
import subprocess
from pathlib import Path


playbooks_dir = Path("ansible-playbooks")
assert playbooks_dir.is_dir()


def setup_participant(username):
    result = subprocess.run(
        ["ansible-playbook", "setup.yml", "-e", f"username={username}"],
        cwd=playbooks_dir,
    )
    print(result.stdout)


def remove_participant(username):
    result = subprocess.run(
        ["ansible-playbook", "remove.yml", "-e", f"username={username}"],
        cwd=playbooks_dir,
    )
    print(result.stdout)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="The username for the participant")
    parser.add_argument("--remove", "-r", action="store_true", help="Delete the user")
    args = parser.parse_args()

    if args.remove:
        remove_participant(args.username)
        sys.exit(0)

    setup_participant(args.username)
