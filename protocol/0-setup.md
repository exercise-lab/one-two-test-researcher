# Before participants arrive

Here are the steps to take before the participants arrive.

## Boot the computers in Ubuntu

In the diagram below, the testing computers are highlighted in **bold**. If a
computer is booted in Windows, restart it and press **F12** when you see the
screen with the Dell logo. On the boot menu, select the drive with the name
**ubuntu**. The system will then boot in Ubuntu.

| left| middle|right |
|----:|------:|:-----|
|    7| **14**|**21**|
|    6|     13|20    |
|    5| **12**|**19**|
|    4|     11|18    |
|    3| **10**|**17**|
|    2|      9|16    |
|    1|      8|15    |

## Fill out the subject info sheet

1. Find out who is coming from the Google Calendar and record
   their names and emails in the subject info sheet.
2. Look up the "go to" language for these participants and record
   it in the subject info sheet.
3. Assign subject ids and computers for the participants.

## Pre-fill consent forms

Using the information you entered on the subject info sheet,
pre-fill the consent forms you will need, noting the participant's
name, subject id, language, and testing computer on each unsigned
consent form.

## Create user accounts for each participant

Go to each computer and create user accounts for the participant. You need to be
logged in to the `lupyanlab` account. Then complete the following steps:

1. Open a terminal (Ctrl+Alt+t) and navigate to the experiment directory.

```
cd ~/experiments/one-two-test
```

1. Make sure the repo is up to date.

```
git pull
```

2. Activate the right version of python in the terminal session.

```
pipenv shell
```

3. Install the experiment for a participant.

```
python run.py -u [subj_id] -l [language]
```

If the subj_id was OTT100 and the language was java, the command would be:

```
python run.py -u OTT100 -l java
```

4. Log out of the lupyanlab account.

## Log in for the participant

1. Log in to their account for them, using their usernames as their passwords.

_Note:_ You may have to click through a welcome screen that pops up because
it's the first time this user has logged on.

2. Open a navigator window (click on the Files app in the sidebar) and navigate
   to the problems directory.

3. Open each of the problems in the expected IDE.

### Java: Eclipse

Using the app launcher (lower left corner of the Ubuntu GUI), open the Eclipse
app. Then import the problem as a Gradle project from the Eclipse app File menu.
Import all of the test problems.

```
File > Import > Gradle project
```

### Python: PyCharm

Using the app launcher (lower left corner of the Ubuntu GUI), open the PyCharm
app. Then open the problem as a Python project from the PyCharm app File menu.
Import all of the test problems.

When opening subsequent projects, select the **Attach** option so that all
projects are opened in the same IDE window.

1. Start the keylogger.

Start the keylogger by opening a terminal window (Ctrl+Alt+t) and entering the
following command:

```
llk
```
