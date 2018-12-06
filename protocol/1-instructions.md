# When a participant arrives

## Consent forms

Give the participant their pre-filled consent form to read and sign. Double
check you have their "go to" language correct. Once they have signed it, bring
them to their assigned computers and have them log in.

## Explain what will happen in the experiment

> You will work on two problems: a hello world problem, and a saddle points
  problem.
> The hello world problem is very simple, you just write a function that
  returns the string "Hello, World". We have you do it so that you can
  get used to running the unit tests which we will use to evaluate your

Show them how to run the tests for the hello world problem, and where to
put their implementation. Tell them to let you know when they have a passing
test.

## Explain the saddle points problem

- Hand them the saddle points problem sheet, and read it to them, asking if
  they understand the problem.
- Have them run the test suite for the saddle points problem, and show them
  where they will put their implementation. Tell them they need to get all
  five tests to pass.
- Tell them they can use the internet to Google things, listen to music while
  they work, and use the problem sheet as scratch paper.
- If they have any questions interpreting the results of the tests, they
  should ask for help.
- Tell them that when they've finished the first 5 tests, they should clean
  up and comment their code, and then they will be given 5 more tests to
  work on.

## Running the tests

**Java: Eclipse**

Run the tests by opening the test file and pressing the green "Play" button in the menu bar. Run the file as a JUnit test.

OR: run the tests from the command line by navigating to the problem directory and running `gradle test`:

```bash
cd ~/problems-java/saddle-points/
gradle test
```

**Python: PyCharm**

Run the tests by opening the test file and selecting "Run 'pytest for test_file_name.py'".

OR: run the tests from the command line by navigating to the problem directory and running `pytest`:

```bash
cd ~/problems-python/saddle-points/
pytest
```
