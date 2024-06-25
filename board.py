class Ship(object):
    '''
    The Ship class represents a piece of a Battleship game.
    '''
    def __init__(self, length, position, orientation):
        """
            Creates a Ship object with the specified length, position, and orientation.
        """
        # Set the attributes
        self.length = int(length)
        self.position = position
        self.orientation = str(orientation)
        self.hit_count = 0
        self.is_sunk = False

    def get_positions(self):
        """
            Returns a list of tuples representing the positions of the ship.
        """
        # Empty list to store positions
        positions = []
        # Add the starting position
        self.position = self.position[0], self.position[1]
        # Add the rest of the positions
        for i in range(self.length):
            # Add the position based on the orientation
            if self.orientation == "h":
                positions.append((self.position[0], self.position[1] + i))
            elif self.orientation == "v":
                positions.append((self.position[0] + i, self.position[1]))
        # Return the positions
        return positions

    def get_orientation(self):
        """
            Returns the orientation of the ship.
        """
        # Return the orientation
        return self.orientation

    def apply_hit(self):
        """
            Increments the hit count of the ship. If the hit count is equal to the length of the ship, the ship is sunk.
        """
        # Increment the hit count
        self.hit_count += 1
        if self.hit_count == self.length:
            # Set the ship to sunk
            self.is_sunk = True


class Board(object):
    """
        The Board class represents a Battleship game board. The board class will keep track of the ships on the board
        and the guesses made by the player.
    """
    def __init__(self, size):
        """
            Creates a Board object with the specified size.
        """
        self.size = size
        # Create the board
        self.board = []
        # Add the rows
        for i in range(size):
            self.board.append([" "] * size)
        self.ships = []


    def place_ship(self, ship):
        """
            Updates the board to include the specified ship.
        """
        # Add the ship to the list of ships
        for position in ship.get_positions():
            # Add the ship to the board
            self.board[position[0]][position[1]] = "S"
        self.ships.append(ship)



    def apply_guess(self, guess):
        """
            Takes a tuple representing a guess and updates the board to include the guess.
        """
        # Check if the guess is a hit or miss
        track = 0
        for ship in self.ships:
            for position in ship.get_positions():
                if position == guess:
                    # Apply the hit
                    ship.apply_hit()
                    # Update the board
                    self.board[guess[0]][guess[1]] = "H"
                    # Print the result
                    print("Hit!")
                    # Set the track to 1
                    track = 1
        if track == 0:
            # Update the board
            self.board[guess[0]][guess[1]] = "M"
            # Print the result
            print("Miss!")



    def validate_ship_coordinates(self, ship):
        """
            This class checks if the ship coordinates are valid. If the coordinates are valid, the method returns True.
        """
        #
        positions = ship.get_positions()
        if positions:
            for row, col in positions:
                # Check if the coordinates are valid
                if row >= self.size or col >= self.size:
                    raise RuntimeError("Ship coordinates are out of bounds!")
                # Check if the coordinates are already taken
                elif self.board[row][col] == "S":
                    raise RuntimeError("Ship coordinates are already taken!")


    def __str__(self):
        """
            Returns a string representation of the board.
        """
        board_str = ""
        # Add the rows
        for row in self.board:
            # Add the columns
            for col in row:
                # Add the column to the string
                board_str += "[" + col + "]"
            board_str += "\n"
        return board_str
