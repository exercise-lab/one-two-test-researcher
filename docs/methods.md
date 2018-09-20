# Methods

## Reproducing

Use pipenv to install the required python packages into a virtualenv.

```bash
pipenv install --dev
```

## Ansible playbooks

### From control machine

configure.yml
: Configure a fresh install of Ubuntu 18.04

install.yml
: Install the one-two-test experiment on each testing computer

### From testing computer

setup.yml
: Create a new user on the testing computer with all the required experiment files.

## Run a participant

```bash
# on lab computer
python3 run.py --username jim --problem bowling --language python
# switch users to jim
```

## Remove a participant

```bash
python3 end.py --username jim
```
