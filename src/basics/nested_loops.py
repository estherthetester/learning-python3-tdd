# Print a staircase of emoji's (1-10) using a while and for loop.


def print_emoji_nested(stairs):
    emojis = ""
    emoji = 1
    for stair in range(1, stairs+1):
        while emoji <= stair:
            emojis += "\U0001f600"
            emoji += 1
        print(emojis)


def test_should_print_emoji_nested(capsys):
    expected = "\U0001f600\n\U0001f600\U0001f600\n"
    print_emoji_nested(2)
    output = capsys.readouterr()

    assert output.out == expected


def print_emoji_for_loop(stairs):

    for stair in range(1, stairs+1):
        print("\U0001f600" * stair)


def test_should_print_emoji_for_loop(capsys):
    expected = "\U0001f600\n\U0001f600\U0001f600\n"
    print_emoji_for_loop(2)
    output = capsys.readouterr()

    assert output.out == expected


def print_emoji_while_loop(stairs):
    stair = 1
    while stair <= stairs:
        print("\U0001f600" * stair)
        stair += 1


def test_should_print_emoji_while_loop(capsys):
    expected = "\U0001f600\n\U0001f600\U0001f600\n"
    print_emoji_while_loop(2)
    output = capsys.readouterr()

    assert output.out == expected


print_emoji_nested(10)
print_emoji_for_loop(10)
print_emoji_while_loop(10)