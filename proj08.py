##############################################
# CSE 231 Project 8
# Algorithm
#   This project is a game of battleship. The user will be prompted to enter the size of the board, the number of ships,
#   and the size of each ship.
#   The user will then be prompted to enter the coordinates of each ship and the orientation of each ship.
#   The user will then be prompted to enter a guess. The game will continue until one player has sunk all the
#   other player's ships.
#   The game will print out the board after each guess.
#   Classes and functions are used to make the game work by validating the user's input and checking if the game is over.
#   The game is played by calling the main function.
#   The main function calls the other functions and classes.
#   The main function is called at the end of the program.
##############################################


from board import Ship, Board #important for the project
from game import Player, BattleshipGame #important for the project


def main():
    board_size = 5
    ship_list = [5, 4, 3, 3, 2]
    # create player 1
    player1_board = Board(board_size)
    # create player 2
    player2_board = Board(board_size)
    # Use Player class to create player 1 and player 2
    player1 = Player("Player 1", player1_board, ship_list)
    player2 = Player("Player 2", player2_board, ship_list)
    # set all ships for player 1
    game = BattleshipGame(player1, player2)
    # play the game
    game.play()

if __name__ == "__main__":
    main()

