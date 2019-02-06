from looping_exercise import loop_through_print_output


def test_should_return_even_numbers(capsys):
    expected = '2 is even'

    loop_through_print_output(2, 2)
    capture = capsys.readouterr()

    assert expected == capture.out.rstrip()


def test_should_return_odd_numbers(capsys):
    expected = '1 is odd'

    loop_through_print_output(1, 1)
    capture = capsys.readouterr()

    assert expected == capture.out.rstrip()


def test_should_return_even_and_odd_numbers(capsys):
    expected = '1 is odd\n2 is even\n3 is odd'

    loop_through_print_output(1, 3)
    capture = capsys.readouterr()

    assert expected == capture.out.rstrip()


def test_should_return_4_as_unlucky_numbers(capsys):
    expected = '4 is unlucky'

    loop_through_print_output(4, 4)
    capture = capsys.readouterr()

    assert expected == capture.out.rstrip()


def test_should_return_odd_even_unlucky_numbers(capsys):
    expected = '1 is odd\n2 is even\n3 is odd\n4 is unlucky'

    loop_through_print_output(1, 4)
    capture = capsys.readouterr()

    assert expected == capture.out.rstrip()


def test_should_return_13_as_unlucky_number(capsys):
    expected = '13 is unlucky'

    loop_through_print_output(13, 13)
    capture = capsys.readouterr()

    assert expected == capture.out.rstrip()


def test_should_return_odd_even_unlucky_numbers(capsys):
    expected = '12 is even\n13 is unlucky\n14 is even'

    loop_through_print_output(12, 14)
    capture = capsys.readouterr()

    assert expected == capture.out.rstrip()
