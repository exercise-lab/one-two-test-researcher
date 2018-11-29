#!/usr/bin/env python
import os
import github3


def create_github_repo(repo):
    github = github3.login(os.environ["GITHUB_USERNAME"], os.environ["GITHUB_PASSWORD"])
    org = github.organization("exercise-lab")
    try:
        org.create_repository(repo, private=True)
    except github3.exceptions.UnprocessableEntity:
        # endpoint already exists
        pass


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", "-r")
    args = parser.parse_args()
    create_github_repo(args.repo)
