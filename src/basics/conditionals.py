from unittest.mock import patch
import random

#Task 1: if choice is 7 print out lucky, otherwise print unlucky
def test_check_lucky(capsys):
    with patch('random.randint', return_value=7):
        check_lucky()
        captured = capsys.readouterr()
        assert "lucky" == captured.out.rstrip()


def test_check_unlucky(capsys):
    with patch('random.randint', return_value=10):
        check_lucky()
        captured = capsys.readouterr()
        assert "unlucky" == captured.out.rstrip()


def check_lucky():
    choice = random.randint(1, 10)
    if choice == 7:
        print("lucky")
    else:
        print("unlucky")


#Task 2: if number is odd print odd otherwise print even
def check_odd():
    num = random.randint(1, 1000)
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


def test_check_odd(capsys):
    with patch('random.randint', return_value=1):
        check_odd()
        captured = capsys.readouterr()
        assert "odd" == captured.out.rstrip()


def test_check_even(capsys):
    with patch('random.randint', return_value=900):
        check_odd()
        captured = capsys.readouterr()
        assert "even" == captured.out.rstrip()



check_lucky()
