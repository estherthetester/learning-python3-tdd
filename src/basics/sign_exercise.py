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


def test_input_both_positive(capsys):
    with patch('random.randint', side_effect=[2, 2]):
        test_x, test_y = exercise_input()
        check_sign(test_x, test_y)
        captured = capsys.readouterr()
        assert "both positive" == captured.out.rstrip()


check_x, check_y = exercise_input()
check_sign(check_x, check_y)

# print("both positive")
# print("both negative")
# print("x is positive and y is negative")
# print("y is positive and x is negative")