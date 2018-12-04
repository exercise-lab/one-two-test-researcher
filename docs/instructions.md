# When a participant arrives

## Consent forms

Give the participant their pre-filled consent form to read and sign. Double
check you have their "go to" language correct. Once they have signed it, bring
them to their assigned computers and have them log in.

## Explain what will happen in the experiment

- You will work on two problems: a hello world problem, and a saddle points
  problem.
- The hello world problem is very simple, you just write a function that
  returns the string "Hello, World", but we have you do it so that you can
  get used to running the unit tests which we will use to evaluate your
  solutions.

You should also know that it's ok to use the internet to Google things,
but please don't try to find exact solutions to the problem you are solving.
It will be really easy for us to tell if you've just copied and pasted in
an entire solution you found somewhere else on the web, but if you need to
look up the docs for a builtin function or something, go right ahead.

Now we will get you set up at your computer, show you how to run the tests,
and let you get started on the first problem. Once you've finished the first
problem, we will come over and you can show us that you can run the tests and
that the tests pass. Then you can start on the second problem.

## Show each participant how to run the tests

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
