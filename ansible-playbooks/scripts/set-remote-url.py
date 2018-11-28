#!/usr/bin/env python
import os
import git


def set_url(dest, repo_name):
    repo = git.Repo(dest)
    url = f"git@github.com:exercise-lab/{repo_name}"
    repo.remotes.origin.set_url(url)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dest", "-d")
    parser.add_argument("--repo", "-r")
    args = parser.parse_args()
    set_url(args.dest, args.repo)
