import clean_your_room as clean
from unittest.mock import patch


def test_should_print_out_message(capsys):
    expected_output = "CLEAN UP YOUR ROOM!"

    clean.print_clean_room()
    capture = capsys.readouterr()

    assert expected_output == capture.out.rstrip()


def test_should_print_out_message_for_given_times(capsys):
    expected_output = "CLEAN UP YOUR ROOM!\nCLEAN UP YOUR ROOM!"

    clean.print_clean_room(2)
    capture = capsys.readouterr()

    assert expected_output == capture.out.rstrip()


def test_should_get_number_of_times_to_tell():
    with patch('builtins.input', return_value = 2):
        test = clean.number_of_times_to_tell()
        assert 2 == test


def test_should_tell_them_to_clean_room_two_times(capsys):
    expected_output = "CLEAN UP YOUR ROOM!\nCLEAN UP YOUR ROOM!"

    with patch('builtins.input', return_value = '2'):
        clean.main()
        capture = capsys.readouterr()
        assert expected_output == capture.out.rstrip()
