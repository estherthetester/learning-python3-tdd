from random import choice, randint


def exercise_inputs():
    actually_sick = choice([True, False])
    kinda_sick = choice([True, False])
    hate_your_job = choice([True, False])
    sick_days = randint(0, 10)
    return actually_sick, kinda_sick, hate_your_job, sick_days


def calling_in_sick(actually_sick, kinda_sick, hate_your_job, sick_days):
    if (actually_sick and sick_days > 0) or (kinda_sick and hate_your_job and sick_days > 0):
        return True
    else:
        return False


def test_calling_in_sick_actually_sick():
    assert calling_in_sick(True, False, True, 10)
    assert calling_in_sick(True, False, False, 10)
    assert calling_in_sick(True, True, False, 10)


def test_calling_in_sick_kinda_sick():
    assert calling_in_sick(False, True, True, 10)
    assert calling_in_sick(True, True, False, 10)


def test_going_to_work_no_leave():
    assert not calling_in_sick(True, False, True, 0)
    assert not calling_in_sick(True, False, False, 0)
    assert not calling_in_sick(True, True, False, 0)
    assert not calling_in_sick(True, True, True, 0)
    assert not calling_in_sick(False, True, False, 0)


def test_going_to_work_love_job():
    assert not calling_in_sick(False, True, False, 10)


# randomly assigns values to these four variables
really_sick, fake_sick, hate_job, days = exercise_inputs()
calling_in_sick(really_sick, fake_sick, hate_job, days)
