#!/usr/bin/env python3
from pathlib import Path
import git


def push_repo(problem):
    repo = git.Repo(problem)

    # check if repo is dirty
    if repo.is_dirty():
        repo.git.add(".")
        repo.git.commit("-m Adding untracked files before push")

    repo.remotes.origin.push()
    repo.git.push("--tags")


if __name__ == "__main__":
    problems = Path(".").glob("*")
    for problem in problems:
        push_repo(problem)
