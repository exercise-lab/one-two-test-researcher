#!/usr/bin/env python
import os
from pathlib import Path

import github3
import jinja2


problem_dir = Path("problems")


env_tmpl = jinja2.Template("""\
export GITHUB_USERNAME={{ username }}
export GITHUB_PASSWORD={{ password }}
""")


def download_problem(github, problem, language):
    language_dir = problem_dir / language
    if not language_dir.is_dir():
        language_dir.mkdir(parents=True)

    repo = github.repository("exercism", language)
    for filename, _ in repo.directory_contents(f"exercises/{problem}"):
        contents = repo.file_contents(f"exercises/{problem}/{filename}")
        if contents.decoded == "":
            print(f"skipping {filename}")
            continue

        with open(language_dir / filename, "wb") as f:
            f.write(contents.decoded)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", "-p", help="the problem to solve")
    parser.add_argument("--language", "-l", help="the language to solve it in")
    args = parser.parse_args()

    username = os.environ.get("GITHUB_USERNAME")
    password = os.environ.get("GITHUB_PASSWORD")
    if username is None or password is None:
        username = input("Enter your GitHub username: ")
        password = input("Enter your GitHub password: ")
        with open(".env", "w") as f:
            f.write(env_tmpl.render(username=username, password=password))

    github = github3.login(username, password)
    download_problem(github, args.problem, args.language)
