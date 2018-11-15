import random
from unittest.mock import patch


# If food is set to either 'apple' or 'grape', your code should print 'fruit'.
# If food is set to either 'bacon' or 'steak', your code should print 'meat'
# If food is set to either 'dirt' or 'worm' your code should print 'yuck'


def food_choice():
    food = random.choice(['apple', 'grape', 'bacon', 'steak', 'worm', 'dirt'])

    if food == 'apple' or food == 'grape':
        print('fruit')
    elif food == 'bacon' or food == 'steak':
        print('meat')
    else:
        print('yuck')


def test_food_choice_fruit(capsys):
    with patch('random.choice', side_effect=['apple', 'grape']):
        food_choice()
        capture = capsys.readouterr()
        assert 'fruit' == capture.out.rstrip()
        food_choice()
        capture = capsys.readouterr()
        assert 'fruit' == capture.out.rstrip()


def test_food_choice_meat(capsys):
    with patch('random.choice', return_value='bacon'):
        food_choice()
        capture = capsys.readouterr()
        assert 'meat' == capture.out.rstrip()


def test_food_choice_other(capsys):
    with patch('random.choice', return_value='worm'):
        food_choice()
        capture = capsys.readouterr()
        assert 'yuck' == capture.out.rstrip()


food_choice()
