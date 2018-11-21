from unittest.mock import patch

PLAYERS = ['Player 1', 'Player 2']


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
        assert test_inputs[0] == get_inputs()[PLAYERS[0]]


def test_same_shoot():
    test_inputs = ['rock', 'rock']
    with patch('builtins.input', side_effect=test_inputs):
        assert "Tie" == get_winner()


def test_player_1_wins():
    test_inputs = ['rock', 'scissors']
    with patch('builtins.input', side_effect=test_inputs):
        assert PLAYERS[0] == get_winner()


def test_player_2_wins():
    test_inputs = ['scissors', 'rock']
    with patch('builtins.input', side_effect=test_inputs):
        assert PLAYERS[1] == get_winner()


def print_intro():
    print('...rock...')
    print('...paper...')
    print('...scissors...')


def get_player_input(player_name):
    player_input = input("(enter " + str(player_name) + "'s choice): ")
    return player_input


def get_inputs():
    player_inputs = {}
    for name in PLAYERS:
        player_inputs[name] = get_player_input(name)
    print("SHOOT!")
    return player_inputs


def get_winner():
    inputs = list(get_inputs().values())
    winner = None
    if inputs[0] == "rock" and inputs[1] == "scissors":
        winner = PLAYERS[0]
    elif inputs[0] == "rock" and inputs[1] == "paper":
        winner = PLAYERS[1]
    elif inputs[0] == "paper" and inputs[1] == "rock":
        winner = PLAYERS[0]
    elif inputs[0] == "paper" and inputs[1] == "scissors":
        winner = PLAYERS[1]
    elif inputs[0] == "scissors" and inputs[1] == "rock":
        winner = PLAYERS[1]
    elif inputs[0] == "scissors" and inputs[1] == "paper":
        winner = PLAYERS[0]
    elif inputs[0] == inputs[1]:
        winner = 'Tie'
    else:
        print("Something went wrong.")
    print_winner(winner)
    return winner


def print_winner(winner):
    if winner != 'Tie':
        print(f"{winner} wins!")
    elif winner == 'Tie':
        print("It's a tie!")
    else:
        print("There should always be a winner, something must have gone wrong.")


get_winner()
