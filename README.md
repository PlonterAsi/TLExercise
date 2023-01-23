# Team Lead Position Exercise

In order to run the project install poetry.

- pip install poetry

Now install the project, from within the project folder run (should install dependencies).

- poetry install

!Note - if depndencies are not install (poetry issues) the run the following:

- pip install pytest pytest-playwright

Playwright needs to be installed before we can work with it

- playwright install

To run the test run the pytest command

- pytest

You can run specific tests like the following

- pytest .\solution\api_automation\
- pytest .\solution\web_automation\
- pytest .\solution\max_single_digit\
