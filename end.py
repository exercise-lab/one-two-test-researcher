import subprocess


def remove_participant(username):
    result = subprocess.run(
        ["ansible-playbook", "remove.yml", "-e", f'{"username":"{username}"}'],
        cwd=playbooks_dir,
    )
    print(result.stdout)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", "-u", help="The username for the participant")
    args = parser.parse_args()
    remove_participant(args.username)
