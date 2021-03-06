#!/usr/bin/env python
import sys
import subprocess
from pathlib import Path


playbooks_dir = Path("ansible-playbooks")
assert playbooks_dir.is_dir()


def setup_participant(username, problems, language):
    result = subprocess.run(
        ["ansible-playbook", "setup.yml", "-e", f'{{"username":"{username}", "language":"{language}"}}'],
        cwd=playbooks_dir,
    )
    print(result.stdout)

    for problem in problems:
        result = subprocess.run(
            ["ansible-playbook", "setup-problem.yml", "-e", f'{{"username":"{username}", "problem":"{problem}", "language":"{language}"}}'],
            cwd=playbooks_dir,
        )
        print(result.stdout)

    if "saddle-points" in problems:
        result = subprocess.run(
            ["ansible-playbook", "setup-saddle-points-helpers.yml", "-e", f'{{"username":"{username}", "problem":"saddle-points", "language":"{language}"}}'],
            cwd=playbooks_dir,
        )
        print(result.stdout)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--username", "-u", help="The username for the participant", required=True)
    parser.add_argument("--problem", "-p", help="The problem to download. Could be more than one. The defaults are the hello-world and saddle-points problems.", nargs="+", default=["hello-world", "saddle-points"])
    parser.add_argument("--language", "-l", help="The language to solve it in", required=True)
    args = parser.parse_args()

    setup_participant(args.username, args.problem, args.language)
