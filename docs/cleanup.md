# One Two Test Experiment

## After a participant is done

### Push their changes to GitHub.

```bash
# Navigate to the problem directory
cd ~/problems-[language]/saddle-points

# See if there are any uncommited changes
git status

# If you see RED when you run `git status`, run the following commands:
git add . && git commit -m "End of experiment"

# If you don't see RED or after you have committed, run the following command:
git push
```

### Teardown the experiment.

1. Log out of the participant's account, and log back in as lupyanlab.
2. Navigate to the experiment directory, and run the stop.py script.

```bash
cd ~/experiments/one-two-test
pipenv shell
python stop.py -u [username]
```
