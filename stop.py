#!/usr/bin/env python
import sys
import subprocess
from pathlib import Path


playbooks_dir = Path("ansible-playbooks")
assert playbooks_dir.is_dir()


def teardown_participant(username, language):
    result = subprocess.run(
            ["ansible-playbook", "teardown.yml", "-e", f'{{"username":"{username}", "language":"{language}"}}'],
        cwd=playbooks_dir,
    )
    print(result.stdout)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--username", "-u", help="The username for the participant", required=True)
    parser.add_argument("--language", "-l", help="The language used by the participant")
    args = parser.parse_args()

    teardown_participant(args.username, args.language)
