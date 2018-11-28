#!/usr/bin/env python
import git
import github3


def create_github_repo(repo):
    github = github3.login(os.environ["GITHUB_USERNAME"], os.environ["GITHUB_PASSWORD"])
    org = github.organization("exercise-lab")
    org.create_repository(repo, private=True)


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
    create_github_repo(args.repo)
    set_url(args.dest, args.repo)
