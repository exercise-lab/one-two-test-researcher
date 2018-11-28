# Running the pilot study

Complete the steps below to set up the computer for a pilot participant.

## Boot the computers in Linux

If you are in Windows, restart the computer and press **F12** when you see the screen with the Dell logo. On the boot menu, select the drive with a name beginning with **WDC**. The system will boot in Linux.

## Setting up for a participant

To set up for a participant, you need to be logged in to the lupyanlab
account. Then complete the following steps:

1. Open a terminal (shortcut: Ctrl+Alt+t) and navigate to the correct experiment directory.

```
cd ~/experiments/pilot
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
              --problem hello-world two-fer saddle-points
python run.py -u pierce -l java -p hello-world two-fer saddle-points
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

3. Open a terminal window and navigate to the problems directory. Show the 
   participant how to run the tests.

```bash
cd ~/problems/
cd hello-world
gradle test
```

4. Open each of the problems in the expected IDE.

**Java: Eclipse**

Using the app launcher (lower left corner of the Ubuntu GUI), open the Eclipse app. Then import the problem as a Gradle project from the Eclipse app File menu.

```
File > Import > Gradle project
```

Run the tests by pressing the green "Play" button in the menu bar.

