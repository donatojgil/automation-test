********Pre-requisite********
------------------------
python 3
virtualenv

This project uses python3 to run the tests.

Install virtualenv
------------------------
Use virtual env to create a python environment outside of your machine's environment.
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



