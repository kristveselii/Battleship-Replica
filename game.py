from board import Ship, Board

import sys


def input(prompt=None):
    if prompt != None:
        print(prompt, end="")
    aaa_str = sys.stdin.readline()
    aaa_str = aaa_str.rstrip("\n")
    print(aaa_str)
    return aaa_str


class Player(object):
    """
        The Player class represents a player in a Battleship game. The player class will keep track of the player's board,
        the player's ships, and the player's guesses.
    """

    def __init__(self, name, board, ship_list):
        """
            add your method header here.
        """
        self.name = name
        self.board = board
        self.ship_list = ship_list
        # list of guesses
        self.guesses = []

    def validate_guess(self, guess):
        """
            Validates the guess. If the guess is valid, the method returns True. If the guess is invalid, the method
        """
        # check if guess is valid
        if guess in self.guesses:
            raise RuntimeError('This guess has already been made!')
        # check if guess is out of bounds
        elif guess[0] >= self.board.size or guess[1] >= self.board.size:
            raise RuntimeError('Guess is not a valid location!')

    def get_player_guess(self):
        """
            Player gets a guess from the user. The guess is validated and returned.
        """
        while True:
            # get guess from user
            user_guess = input('Enter your guess: ')
            # check if guess is valid
            try:
                # split guess into coordinates
                guess = user_guess.split(',')
                # check if guess is valid
                if len(guess) != 2 or '' in guess:
                    raise RuntimeError('Guess is not a valid location!')
                # convert guess to tuple
                guess = (int(guess[0]), int(guess[1]))
                # check if guess is valid
                Player.validate_guess(self, guess)
                return guess
            # handle errors
            except RuntimeError as e:
                print(e)
            except ValueError:
                print('Guess is not a valid location!')
                continue

    def set_all_ships(self):
        """
        Set all ships for the player.
        """
        # set all ships
        for ship in self.ship_list:
            while True:
                try:
                    # get coordinates and orientation from user
                    coordinates = input('Enter the coordinates of the ship of size ' + str(ship) + ': ')
                    orientation = input('Enter the orientation of the ship of size ' + str(ship) + ': ')
                    # split coordinates into row and column
                    location = coordinates.split(',')
                    # create ship object
                    coordinates_tuple = (int(location[0]), int(location[1]))
                    new_ship = Ship(ship, coordinates_tuple, orientation)
                    # validate ship
                    self.board.validate_ship_coordinates(new_ship)
                    self.board.place_ship(new_ship)
                    break
                # handle errors
                except Exception as e:
                    print(e)
                    continue


class BattleshipGame(object):
    """
        BattleshipGame class is used to play the game and check if the game is over.
    """

    def __init__(self, player1, player2):
        """
            add your method header here.
        """
        self.player1 = player1
        self.player2 = player2

    def check_game_over(self):
        """
            Checks if the game is over. If the game is over, the method returns the name of the winner.
        """

        # check if all ships are sunk
        player1_ships = True
        player2_ships = True
        # check if all ships are sunk
        for ship in self.player1.board.ships:
            if not ship.is_sunk:
                # set player1_ships to False
                player1_ships = False
        for ship in self.player2.board.ships:
            if not ship.is_sunk:
                # set player2_ships to False
                player2_ships = False
        # check if all ships are sunk
        if player1_ships:
            return 'Player 2'
        elif player2_ships:
            return 'Player 1'
        else:
            return None

    def display(self):
        """
            Displays the boards of both players.
        """
        print("Player 1's board:")
        print(self.player1.board)
        print("Player 2's board:")
        print(self.player2.board)

    def play(self):
        """
            Plays the game until one player has sunk all the other player's ships.
        """
        Player.set_all_ships(self.player1)
        Player.set_all_ships(self.player2)

        while True:
            # display boards
            BattleshipGame.display(self)
            print(f'{self.player1.name}\'s turn.')
            player1_guess = Player.get_player_guess(self.player1)
            # apply guess
            Board.apply_guess(self.player2.board, player1_guess)
            # check if game is over
            if self.check_game_over() == 'Player 1':
                print('Player 1 wins!')
                break
            print(f'{self.player2.name}\'s turn.')
            # get guess from player2
            player2_guess = Player.get_player_guess(self.player2)
            # apply guess
            Board.apply_guess(self.player1.board, player2_guess)
            # check if game is over
            continue_playing = input('Continue playing?: ')
            if self.check_game_over() == 'Player 2':
                print('Player 2 wins!')
                break
            if continue_playing == 'q':
                break
            else:
                continue
