#!/usr/bin/env python
import os
import git
import github3


def connect_to_github():
    username = os.environ["GITHUB_USERNAME"]
    password = os.environ["GITHUB_PASSWORD"]
    github = github3.login(username, password)
    return github


if __name__ == "__main__":
    github = connect_to_github()
    github_org = github.organization("exercise-lab")
    saddle_points_repos = [github_repo for github_repo in github_org.repositories()
                           if "saddle-points-OTT" in github_repo.name]

    experiment_repo = git.Repo(".")
    existing_submodule_urls = [submodule.url for submodule in experiment_repo.submodules]

    for github_repo in saddle_points_repos:
        src = f"git@github.com:exercise-lab/{github_repo.name}.git"
        if src not in existing_submodule_urls:
            subj_id = github_repo.name.split("-")[-1]
            language = github_repo.name.replace("one-two-test-", "").split("-")[0]
            dst = f"solutions/{language}/{subj_id}"

            try:
                experiment_repo.git.submodule("add", src, dst)
            except git.GitCommandError as e:
                print(f"unable to add repo from subj_id {subj_id}: {e}")
