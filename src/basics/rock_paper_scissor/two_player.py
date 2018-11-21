from unittest.mock import patch

PLAYERS = ['Player 1', 'Player 2']


def print_intro():
    print('...rock...')
    print('...paper...')
    print('...scissors...')


def get_player_input(player_name):
    player_input = input("(enter " + str(player_name) + "'s choice): ")
    return player_input


def test_print_intro(capsys):
    print_intro()
    capture = capsys.readouterr()
    assert "...rock...\n...paper...\n...scissors...\n" == capture.out


def test_player_1_input():
    with patch('builtins.input', return_value='rock'):
        test_name = 'Player 1'
        assert 'rock' == get_player_input(test_name)


def test_get_input():
    test_inputs = ['rock', 'paper']
    with patch('builtins.input', side_effect=test_inputs):
        assert test_inputs == play_game()


def play_game():
    inputs = []
    for name in PLAYERS:
        inputs.append(get_player_input(name))
    print("SHOOT!")
    return inputs


play_game()
