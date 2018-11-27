#!/usr/bin/env python
import os
from pathlib import Path

import git
import github3
import jinja2


problem_dir = Path("problems")


env_tmpl = jinja2.Template("""\
export GITHUB_USERNAME={{ username }}
export GITHUB_PASSWORD={{ password }}
""")

def create_problem_repo(problem, language):
    repo = git.Repo.init(problem_dir / language / "exercises" / problem)
    return repo

def download_problem(github, problem, language):
    repo = github.repository("exercism", language)
    download_files_in_github_repo(repo, f"exercises/{problem}", problem_dir / language)

def commit_problem_files(repo):
    repo.git.add(".")
    repo.git.commit("-m 'Initial commit'")

def push_problem_to_github(github, repo, repo_name):
    org = github.organization("exercise-lab")
    org.create_repository(repo_name, private=True)
    repo.create_remote("origin", f"git@github.com:exercise-lab/{repo_name}.git")
    repo.git.push("-u", "origin", "master")

def download_files_in_github_repo(repo, dir_path, language_dir):
    for filename, contents in repo.directory_contents(dir_path):
        if contents.type == "dir":
            # recurse through subdirectories
            download_files_in_github_repo(repo, contents.path, language_dir)
        elif contents.type == "file":
            file_contents = repo.file_contents(contents.path)
            if file_contents.decoded == "":
                print(f"skipping empty file '{file_contents.path}'")
                continue

            dst = language_dir / file_contents.path
            if not dst.parent.is_dir():
                dst.parent.mkdir(parents=True)

            with open(dst, "wb") as f:
                f.write(file_contents.decoded)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", "-p", help="the problem to solve", required=True)
    parser.add_argument("--language", "-l", help="the language to solve it in", required=True)
    args = parser.parse_args()

    username = os.environ.get("GITHUB_USERNAME")
    password = os.environ.get("GITHUB_PASSWORD")
    if username is None or password is None:
        username = input("Enter your GitHub username: ")
        password = input("Enter your GitHub password: ")
        with open(".env", "w") as f:
            f.write(env_tmpl.render(username=username, password=password))

    github = github3.login(username, password)
    repo = create_problem_repo(args.problem, args.language)
    download_problem(github, args.problem, args.language)
    commit_problem_files(repo)
    repo_name = f"one-two-test-{args.language}-{args.problem}"
    push_problem_to_github(github, repo, repo_name)
