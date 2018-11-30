# One Two Test Experiment

### Switching from part1 to part2

When a participant has finished part1, open a terminal window (Ctrl+Alt+T) and follow these steps to start them on part2.

```bash
# Navigate to the problem directory
cd ~/problems-[language]/saddle-points

# See if there are any uncommited changes
git status

# If you see RED when you run `git status`, run the following commands:
git add . && git commit -m "Finished part1"

# If you don't see RED or after you have committed, run the following commands:
git tag part1done
git merge -m "Add part2" origin/part2

# Open up the new part2 tests file for the participant
```
