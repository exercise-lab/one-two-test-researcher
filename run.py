#!/usr/bin/env python
import sys
import subprocess
from pathlib import Path


playbooks_dir = Path("ansible-playbooks")
assert playbooks_dir.is_dir()


def setup_participant(username):
    result = subprocess.run(
        ["ansible-playbook", "setup.yml", "-e", f'{{"username":"{username}", "problem":"{problem}", "language":"{language}"}}'],
        cwd=playbooks_dir,
    )
    print(result.stdout)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--username", "-u", help="The username for the participant")
    parser.add_argument("--problem", "-p", help="The problem to download")
    parser.add_argument("--language", "-l", help="The language to solve it in")
    args = parser.parse_args()

    setup_participant(args.username)
