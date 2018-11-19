from random import choice, randint, seed
from unittest.mock import patch


def exercise_inputs():
    actually_sick = choice([True, False])
    kinda_sick = choice([True, False])
    hate_your_job = choice([True, False])
    sick_days = randint(0, 10)
    return actually_sick, kinda_sick, hate_your_job, sick_days


def calling_in_sick(actually_sick, kinda_sick, hate_your_job, sick_days):
    if actually_sick and sick_days > 0:
        return True


def test_calling_in_sick():
    with patch('boolean_exercise.choice', side_effect=[True, True, True]):
        seed(1)
        test_actually_sick, test_kinda_sick, test_hate_your_job, test_sick_days = exercise_inputs()
        assert calling_in_sick(test_actually_sick, test_kinda_sick, test_hate_your_job, test_sick_days)



# randomly assigns values to these four variables
actually_sick, kinda_sick, hate_your_job, sick_days = exercise_inputs()
calling_in_sick(actually_sick, kinda_sick, hate_your_job, sick_days)