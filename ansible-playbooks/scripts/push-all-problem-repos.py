#!/usr/bin/env python
from pathlib import Path
import git


def push_repo(problem):
    repo = git.Repo(problem)

    # check if repo is dirty

    repo.remotes.origin.push()


if __name__ == "__main__":
    problems = Path(".").listdir()
    for problem in problems:
        push_repo(problem)
