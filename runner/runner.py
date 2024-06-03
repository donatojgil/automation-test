import pytest


def main():
    """
        Triggers the automation
        :return: 0 for success. 1 For errors.
        :rtype: tuple
        """

    result = pytest.main(["-s", '--disable-warnings', "./tests/test_ali.py"])
    if int(result) == 1:
        return 1, "Failed at Searching"
    


if __name__ == '__main__':
    main()
