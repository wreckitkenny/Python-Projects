__author__ = "Wreck-it Kenny"
__copyright__ = "Copyright 2019, The Python Project"
__version__ = "1.0"
__email__ = "tung.tran.3295@gmail.com"
__status__ = "Production"

# Import Modules
import itertools


# Function to play game
def play_game(current, player=0, row=0, column=0, display=False):
    print("   " + "  ".join([str(i) for i in range(game_size)]))
    if not display:
        current[row][column] = player
    for count, row in enumerate(current):
        print(count, row)
    return current


# Function to determine who is winner
def winner(current):
    # Horizontal Winner
    for row in current:
        if row.count(row[0]) == len(current[0]) and row[0] != 0:
            print(f"Play {row[0]} is the horizontal winner.")
            return True

    # Vertical Winner
    for col in range(len(current[0])):
        check = []
        for row in current:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the vertical winner.")
            return True

    #  Diagonal Winner
    #  Case(\):
    # if current[0][0] == current[1][1] == current[2][2]:
    #     print("Winner")
    diags = []
    for row, col in enumerate(range(len(current[0]))):
        diags.append(current[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the diagonal winner (\\)")
        return True

    # Case(/):
    # if current[0][2] == current[1][1] == current[2][0]:
    #     print("Winner")
    diags = []
    for row, col in enumerate(reversed(range(len(current[0])))):
        diags.append(current[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the diagonal winner (/)")

    return False


play = True
players = [1, 2]
while play:

    game_size = int(input("What size game TicTacToe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    won = False
    player_cycle = itertools.cycle(players)
    play_game(game, display=True)
    while not won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print(f"Current player is {current_player}")
            column_choice = int(input("Choose column: "))
            row_choice = int(input("Choose row: "))
            played = play_game(game, player=current_player, row=row_choice,
                               column=column_choice)

        if winner(game):
            won = True
            restart = input("Would you like to play again? ")
            if restart.lower() == "y":
                print("Restarting!")
            elif restart.lower() == "n":
                print("Good bye")
                play = False
            else:
                print("Invalid answer.")
                play = False
