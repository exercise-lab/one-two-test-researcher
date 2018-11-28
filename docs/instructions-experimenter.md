# Running the One Two Test experiment

Complete the steps below to set up the computer for a participant in the One Two Test experiment.

## Boot the computers in Ubuntu

If you are in Windows, restart the computer and press **F12** when you see the screen with the Dell logo. On the boot menu, select the drive with the name **ubuntu**. The system will boot in Ubuntu.

## Setting up for a participant

To set up for a participant, you need to be logged in to the lupyanlab
account. Then complete the following steps:

1. Open a terminal (shortcut: Ctrl+Alt+t) and navigate to the correct experiment directory.

```
cd ~/experiments/one-two-test
```

2. Activate the right version of python in the terminal session

```
pipenv shell
```

3. Install the experiment for a participant.

```
python run.py --help
python run.py --username pierce \
              --language java   \
              --problem hello-world saddle-points
python run.py -u pierce -l java -p hello-world saddle-points
```

**Summary**

```
cd ~/experiment/pilot
pipenv shell
python run.py -u [username] -l [language] -p [problem1] [problem2] [...]
```

After the run.py script completes, log out of the lupyanlab account and wait until the participant arrives.

## Logging in for a participant

When a participant arrives for the experiment, complete the following:

1. Log in to their account for them, using their usernames as their passwords.

_Note:_ You may have to click through a welcome screen that pops up because
it's the first time this user has logged on.

2. Open a navigator window (click on the Files app in the sidebar) and navigate
   to the problems directory.

3. Open each of the problems in the expected IDE.

**Java: Eclipse**

Using the app launcher (lower left corner of the Ubuntu GUI), open the Eclipse app. Then import the problem as a Gradle project from the Eclipse app File menu.

```
File > Import > Gradle project
```

Run the tests by opening the test file and pressing the green "Play" button in the menu bar. Run the file as a JUnit test.

**Python: PyCharm**

Using the app launcher (lower left corner of the Ubuntu GUI), open the PyCharm app. Then open the problem as a Python project from the PyCharm app File menu.

Run the tests by opening the test file and selecting "Run 'pytest for test_file_name.py'".
