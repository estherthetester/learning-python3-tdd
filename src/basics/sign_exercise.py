# If both are positive numbers, print "both positive".
# If both are negative, print "both negative".
# Otherwise, tell us which one is positive and which one is negative, e.g. "x is positive and y is negative"

import random
from unittest.mock import patch


def exercise_input():
    x = random.randint(-100, 100)
    while x == 0:  # make sure x isn't zero
        x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    while y == 0:  # make sure y isn't zero
        y = random.randint(-100, 100)
    return x, y


def check_sign(x, y):
    if (x % 2 == 0) and (y % 2 == 0):
        print("both positive")
    elif not (x % 2 == 0) and not (y % 2 == 0):
        print("both negative")
    elif (x % 2 == 0) and not (y % 2 == 0):
        print("x is positive and y is negative")
    else:
        print("y is positive and x is negative")


def test_input_both_positive(capsys):
    with patch('random.randint', side_effect=[2, 2]):
        test_x, test_y = exercise_input()
        check_sign(test_x, test_y)
        captured = capsys.readouterr()
        assert "both positive" == captured.out.rstrip()


def test_input_both_negative(capsys):
    with patch('random.randint', side_effect=[3, 3]):
        test_x, test_y = exercise_input()
        check_sign(test_x, test_y)
        captured = capsys.readouterr()
        assert "both negative" == captured.out.rstrip()


def test_input_x_positive_y_negative(capsys):
    with patch('random.randint', side_effect=[2, 3]):
        test_x, test_y = exercise_input()
        check_sign(test_x, test_y)
        captured = capsys.readouterr()
        assert "x is positive and y is negative" == captured.out.rstrip()


def test_input_y_positive_x_negative(capsys):
    with patch('random.randint', side_effect=[3, 2]):
        test_x, test_y = exercise_input()
        check_sign(test_x, test_y)
        captured = capsys.readouterr()
        assert "y is positive and x is negative" == captured.out.rstrip()


check_x, check_y = exercise_input()
check_sign(check_x, check_y)