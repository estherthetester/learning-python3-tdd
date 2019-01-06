import clean_your_room as clean


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

