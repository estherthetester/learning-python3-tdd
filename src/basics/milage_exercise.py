from unittest.mock import patch

MILES_KM = 1.60934


def test_km_input():
    with patch('builtins.input', side_effect=['50']):
        kms = kms_to_miles()
        assert kms[0] == '50'


def test_km_to_miles():
    with patch('builtins.input', side_effect=['50']):
        miles = kms_to_miles()
        assert int(miles[1]) == 31


def test_round_miles():
    with patch('builtins.input', side_effect=['50']):
        miles = kms_to_miles()
        assert miles[1] == 31.07


def kms_to_miles():
    print("How many kilometers have you cycled today?")
    kms = input()
    miles = round(float(kms)/MILES_KM, 2)
    print(f"Your {kms}km ride is equal to {miles}mi")
    return kms, miles

kms_to_miles()