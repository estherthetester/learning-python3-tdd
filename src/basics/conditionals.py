#Task: if choice is 7 print out lucky, otherwise print unlucky

import unittest.mock as mock
import random


def test_check_lucky(capsys):
    with mock.patch('random.randint', return_value=7):
        check_lucky()
        captured = capsys.readouterr()
        assert "lucky" == captured.out.rstrip()


def test_check_unlucky(capsys):
    with mock.patch('random.randint', return_value=10):
        check_lucky()
        captured = capsys.readouterr()
        assert "unlucky" == captured.out.rstrip()


def check_lucky():
    choice = random.randint(1, 10)
    if choice == 7:
        print("lucky")
    else:
        print("unlucky")


check_lucky()
