# Methods

## Reproducing

Use pipenv to install the required python packages into a virtualenv.

```bash
pipenv install --dev
```

## Install the experiment

First install the experiment on all of the lab computers.

```bash
# on control machine
cd ansible-playbooks
ansible-playbook install.yml
```

## Run a participant

```bash
# on lab computer
python3 run.py test1
```

## Remove a participant

```bash
python3 run.py --remove test1
```
