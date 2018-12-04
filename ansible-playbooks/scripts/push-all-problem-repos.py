#!/usr/bin/env python3
from pathlib import Path
import git


def push_repo(problem):
    repo = git.Repo(problem)

    # check if repo is dirty
    if repo.is_dirty():
        repo.git.add(".")
        repo.git.commit("Adding untracked files before push")

    repo.remotes.origin.push()


if __name__ == "__main__":
    problems = Path(".").listdir()
    for problem in problems:
        push_repo(problem)
