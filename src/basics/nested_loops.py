# Print a staircase of emoji's (1-10) using a while and for loop.


SMILE_FACE = "\U0001f600"
SMILE_FACE_STAIRCASE = SMILE_FACE + "\n" + SMILE_FACE + SMILE_FACE + "\n"
SMILE_FACE_CENTRED = " " + SMILE_FACE + " " + "\n" + \
                     SMILE_FACE + SMILE_FACE + "\n"

#Learning: using string multiplication means we can reduce the function from 8 lines to 3.
def print_emoji_nested(stairs):
    emojis = ""
    emoji = 1
    for stair in range(1, stairs+1):
        while emoji <= stair:
            emojis += SMILE_FACE
            emoji += 1
        print(emojis)


def test_should_print_emoji_nested(capsys):
    expected = SMILE_FACE_STAIRCASE
    print_emoji_nested(2)
    output = capsys.readouterr()

    assert output.out == expected


def print_emoji_for_loop(stairs):

    for stair in range(1, stairs+1):
        print(SMILE_FACE * stair)


def test_should_print_emoji_for_loop(capsys):
    expected = SMILE_FACE_STAIRCASE
    print_emoji_for_loop(2)
    output = capsys.readouterr()

    assert output.out == expected


def print_emoji_while_loop(stairs):
    stair = 1
    while stair <= stairs:
        print(SMILE_FACE * stair)
        stair += 1


def test_should_print_emoji_while_loop(capsys):
    expected = SMILE_FACE_STAIRCASE
    print_emoji_while_loop(2)
    output = capsys.readouterr()

    assert output.out == expected


def print_emoji_centred(stairs):
    for stair in range(1, stairs+1):
        offset = " " * (stairs - stair)
        print(offset + (SMILE_FACE * stair) + offset)


def test_should_print_emoji_centred(capsys):
    expected = SMILE_FACE_CENTRED
    print_emoji_centred(2)
    output = capsys.readouterr()

    assert output.out == expected


print_emoji_nested(10)
print_emoji_for_loop(10)
print_emoji_while_loop(10)
print_emoji_centred(10)