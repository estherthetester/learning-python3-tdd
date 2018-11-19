def print_intro():
    print('...rock...')
    print('...paper...')
    print('...scissors...')


def test_print_intro(capsys):
    print_intro()
    capture = capsys.readouterr()
    assert "...rock...\n...paper...\n...scissors...\n" == capture.out
