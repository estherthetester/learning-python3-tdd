from unittest.mock import patch

PLAYERS = ['Player 1', 'Player 2']


def test_print_intro(capsys):
    print_intro()
    capture = capsys.readouterr()
    assert capture.out == "...rock...\n...paper...\n...scissors...\n"


def test_player_1_input():
    with patch('builtins.input', return_value='rock'):
        test_name = 'Player 1'
        assert get_player_input(test_name) == 'rock'


def test_get_input():
    test_inputs = ['rock', 'paper']
    with patch('builtins.input', side_effect=test_inputs):
        assert get_inputs()[PLAYERS[0]] == test_inputs[0]


def test_same_shoot():
    test_inputs = ['rock', 'rock']
    with patch('builtins.input', side_effect=test_inputs):
        assert get_winner() == "Tie"


def test_player_1_wins():
    test_inputs = ['rock', 'scissors']
    with patch('builtins.input', side_effect=test_inputs):
        assert get_winner() == PLAYERS[0]


def test_player_2_wins():
    test_inputs = ['scissors', 'rock']
    with patch('builtins.input', side_effect=test_inputs):
        assert get_winner() == PLAYERS[1]


def test_player_1_wins_scissors():
    test_inputs = ['scissors', 'paper']
    with patch('builtins.input', side_effect=test_inputs):
        assert get_winner() == PLAYERS[0]


def test_incorrect_input():
    test_inputs = ['dfgkljdg', 'kdjfhgk']
    with patch('builtins.input', side_effect=test_inputs):
        assert get_winner() is None


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
    if inputs[0] == inputs[1]:
        winner = 'Tie'
    elif inputs[0] == "rock":
        if inputs[1] == "scissors":
            winner = PLAYERS[0]
        if inputs[1] == "paper":
            winner = PLAYERS[1]
    elif inputs[0] == "paper":
        if inputs[1] == "rock":
            winner = PLAYERS[0]
        if inputs[1] == "scissors":
            winner = PLAYERS[1]
    elif inputs[0] == "scissors":
        if inputs[1] == "rock":
            winner = PLAYERS[1]
        if inputs[1] == "paper":
            winner = PLAYERS[0]
    else:
        print("Something went wrong.")
    print_winner(winner)
    return winner


def print_winner(winner):
    if winner == 'Tie':
        print("It's a tie!")
    elif winner is not None:
        print(f"{winner} wins!")
    else:
        print("There should always be a winner, something must have gone wrong.")


get_winner()
