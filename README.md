# Test Marvel API with Behave
Using [Behave](https://behave.readthedocs.io/) to implement tests in the [Marvel API](https://developer.marvel.com/docs) with success and exception cases.

### Create the virtual environment with [venv](https://docs.python.org/3/library/venv.html):

    python -m venv venv

### Start the virtual environment in venv:

    .\venv\Scripts\Activate.ps1 # Windows
    source venv/bin/activate    # Linux

### Install project dependencies

    pip install -r requirements.txt

### Get Authorization Credentials in the Marvel API

[Marvel Developer Site](https://developer.marvel.com/account)

### Set environment variables with [python-dotenv CLI](https://pypi.org/project/python-dotenv/):

    dotenv set API_URL https://gateway.marvel.com:443

    dotenv set PUBLIC_KEY {your_public_key}

    dotenv set PRIVATE_KEY {your_private_key}


### To verify that the creation of the variables was successful, you can run this command in the python-dotenv CLI:

    dotenv list --format=simple

It is also possible to see their creation in the generated `.env` file

### Test Cases
**Feature:** GET Characters

**Scenario:** Get and list chracters by characterid on Marvel API (Using Scenario Outlines to pass three data sets).

**Scenario:** Get a nonexistent character by characterid on Marvel API (negative scenario to catch exception).

**Feature:** GET Stories

**Scenario:** Get and list five stories on Marvel API.

### Run test scenarios

    behave -f pretty
    behave --tags="@positive" features/ # Positive Scenarios
    behave --tags="@negative" features/ # Negative Scenarios

### Project structure

```
features
features/*.feature

features/steps
features/steps/*./steps.py

behave.ini

reports
```

### What's in each file?

| File | What is |
| ------- | ----------------- |
| *.feature | Gherking file containing execution rules|
| behave.ini | Project config |
| environment.py | Project hooks |
| /steps/*.py | Files with steps implementation |
| reports | Reports folder generated after execution |
