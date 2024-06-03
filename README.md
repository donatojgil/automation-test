********Pre-requisite********
------------------------
python 3
virtualenv
Allure Report: https://allurereport.org/docs/install/

This project uses python3 to run the tests.

Install virtualenv
------------------------
Use virtual env to create a python environment outside your machine's environment.
I followed https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3


Running using the runner
------------------------

There is a runner that should be used to invoke any test(s)

``python3 ./runner/runner.py``


Running Local Tests
------------------------------------------------
``pip3 install -r requirements.txt`` to install libraries


### Run Specific Test
``pytest <test> -s``

``-s`` is added to be able to print to console

``-r fp`` is also a good option to add since it prints a list of passed/failed tests after all tests are run

``-m <TAG>`` to run tests with a specific tag. E.g. ``pytest -s -m <TAG>``

Allure Reports
------------------------------------------------

Allure report is available for each test run in /report folder. Run in order:

``pytest --alluredir=./report ./tests/test_ali.py``
``allure serve ./report``

<a href="https://ibb.co/LvK6VG2"><img src="https://i.ibb.co/Ybg8Hrq/Screenshot-2024-06-03-at-6-42-34-PM.png" alt="Screenshot-2024-06-03-at-6-42-34-PM" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'>things png</a><br />
