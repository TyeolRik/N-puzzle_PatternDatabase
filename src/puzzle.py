""" This module is about Puzzle Class

- Generate Puzzle by getting user's input (size of puzzle)
- Default Puzzle is 15-puzzle.
- Make all possible puzzles.
- Move blank.
"""

import math
import numpy as np

_BLANK = '*'

def swap(x, y):
    temp = x
    x = y
    y = temp

def distance(point1, point2):
    """
    Args:
        point1: ex) (1,1), (2,3)
        point2: ex) (1,1), (2,3)

    Returns:
        sqrt((x2-x1)**2 - (y2-y1)**2)

    Example:
        >>> distance((1,1) (2,2))
        >>> 1.4142135623730951
    """
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    # return distance(point1[0], point1[1], point2[0], point2[1])

def get_number_of_inversions(puzzle_1d_array):
    """
    What is an Inversion?
        If we assume the tiles written out in a single row (1D Array) instead of being spread in N-rows (2D Array),
        a pair of tiles (a, b) form an inversion if a appears before b but a > b.
    """
    number_of_inversions = 0
    # Check Inversion
    for i in range(0, len(puzzle_1d_array)):
        if puzzle_1d_array[i] != _BLANK:
            for j in range(i, len(puzzle_1d_array)):
                if puzzle_1d_array[j] != _BLANK:
                    # print(puzzle_1d_array[i], " compare ", puzzle_1d_array[j])
                    if puzzle_1d_array[i] > puzzle_1d_array[j]:
                        number_of_inversions = number_of_inversions + 1
    return number_of_inversions

class Puzzle:
    row = 4
    column = 4
    size_of_puzzle = 16
    puzzle = []

    def __init__(self, number_of_row, number_of_column):
        """
        Args:
            number_of_row: The Number of Row.
            number_of_column: The Number of Column.
        """
        self.row = number_of_row
        self.column = number_of_column
        self.size_of_puzzle = number_of_row * number_of_column

    @classmethod
    def with_square_number(cls, square_number):
        """
        Args:
            square_number: This argument should be some number's square like 16, 25, 36, etc.
        """
        if int(square_number) == square_number:
            sqrt_of_square_number = math.sqrt(square_number)
            if int(sqrt_of_square_number) == sqrt_of_square_number:
                return cls(int(sqrt_of_square_number), int(sqrt_of_square_number))
            else:
                print("Argument(square_number): ", square_number, " is not squared value. Please check again")
        else:
            print("Argument(square_number): ", square_number, " is not Int value. Please check again")

    @classmethod
    def with_puzzle(cls, puzzle):
        """
        Args:
            puzzle: It doesn't matter whether argument is 1D or 2D. But, If this is 1D-array, puzzle is considered sqrt(n) x sqrt(n) puzzle.
        """
        dimension = len(np.shape(puzzle))
        if dimension == 1: # If input argument was 1-dimension array
            if math.sqrt(len(puzzle)) == int(math.sqrt(len(puzzle))): # Check length of puzzle is square number
                cls.column = cls.row = int(math.sqrt(len(puzzle)))
                puzzle_2_dimension = [[0 for j in range(cls.column)] for i in range(cls.row)]
                for i in range(cls.row):
                    for j in range(cls.column):
                        puzzle_2_dimension[i][j] = puzzle[i * cls.row + j]
                cls.puzzle = puzzle_2_dimension
                return cls(cls.row, cls.column)
            else:
                print("Puzzle:ClassMethod:with_puzzle :: Input Array length was wrong. Lenght: ", len(puzzle))
        elif dimension == 2:
            cls.row = np.shape(puzzle)[0]
            cls.column = np.shape(puzzle)[1]
            cls.puzzle = puzzle
            return cls(cls.row, cls.column)

    def set_puzzle(self, puzzle):
        """
        Set puzzle with array argument which is 1-Dimension

        Args:
            puzzle_1_dimension: This puzzle array should be 1 dimension.
        """
        self.size_of_puzzle = len(puzzle_1_dimension)
        self.column = self.row = int(math.sqrt(self.size_of_puzzle))
        puzzle_2_dimension = [[0 for j in range(self.column)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.column):
                puzzle_2_dimension[i][j] = puzzle_1_dimension[i * self.row + j]
        self.puzzle = puzzle_2_dimension
        return self

    def make_puzzle(self):
        self.puzzle = [[i*self.column+j+1 for j in range(self.column)] for i in range(self.row)]
        self.puzzle[self.row - 1][self.column - 1] = _BLANK # Last Index should be blank(== _BLANK like `*`)
        return self

    def shuffle(self):

        return self

    def move_tile_with_number(self, to):
        """
        Args:
            to: This argument should be "Near tile" from blank. Distance should be 1

        Example:
            >>> puzzle.make_puzzle().move_tile_with_number(20).pretty_print()
            >>> ===============================
                |  1  |  2  |  3  |  4  |  5  |
                |  6  |  7  |  8  |  9  | 10  |
                | 11  | 12  | 13  | 14  | 15  |
                | 16  | 17  | 18  | 19  |  *  |
                | 21  | 22  | 23  | 24  | 20  |
                ===============================
        """
        blank_x, blank_y = self.find_blank()
        to_x, to_y = self.find_number(to)
        if distance(self.find_blank(), self.find_number(to)) == 1:
            self.puzzle[blank_x][blank_y], self.puzzle[to_x][to_y] = self.puzzle[to_x][to_y], self.puzzle[blank_x][blank_y] # swap blank and object
        else:
            print("You are trying to move wrong tile. Check again")
            print("Blank is now (",blank_x, ", " , blank_y, ")")
            print("Changing Tile is ", to, " Coordinate is (", to_x, ", " , to_y, ")")
        return self

    def move_tile_with_direction(self, to):
        """
        Args:
            to: The direction where blank goes to. Case doesn't matter. "up", "Up", "UP", "uP", "u", "U" is same.

        Example:
            >>> puzzle.make_puzzle().move_tile_with_direction("up").pretty_print()
            >>> ===============================
                |  1  |  2  |  3  |  4  |  5  |
                |  6  |  7  |  8  |  9  | 10  |
                | 11  | 12  | 13  | 14  | 15  |
                | 16  | 17  | 18  | 19  |  *  |
                | 21  | 22  | 23  | 24  | 20  |
                ===============================
        """
        to = to.lower()
        direction = {"up", "down", "right", "left"}
        blank_x, blank_y = self.find_blank()
        if (to.lower() == "up") or (to == "u"):
            self.move_tile_with_number(self.puzzle[blank_x - 1][blank_y])
            return self
        elif (to == "down") or (to == "d"):
            self.move_tile_with_number(self.puzzle[blank_x - 1][blank_y])
            return self
        elif (to == "right") or (to == "r"):
            self.move_tile_with_number(self.puzzle[blank_x - 1][blank_y])
            return self
        elif (to == "left") or (to == "l"):
            self.move_tile_with_number(self.puzzle[blank_x - 1][blank_y])
            return self
    
    def find_blank(self):
        for i in range(self.row):
            for j in range(self.column):
                if self.puzzle[i][j] == _BLANK:
                    return i, j
    
    def find_number(self, number_or_asterisk_to_find):
        """
        Args:
            number_or_asterisk_to_find: ex) 0, 1, 2, ..., _BLANK
        """
        for i in range(self.row):
            for j in range(self.column):
                if self.puzzle[i][j] == number_or_asterisk_to_find:
                    return i, j

    def is_solvable(self):
        """This method is for checking this puzzle is solvable or not. (Only works in Square puzzle)
        In general, for a given grid of width N, we can find out check if a N*N – 1 puzzle is solvable or not by following below simple rules :
            1. If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
            2. If N is even, puzzle instance is solvable if
                - the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is odd.
                - the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is even.
            3. For all other cases, the puzzle instance is not solvable.
        What is an Inversion
            If we assume the tiles written out in a single row (1D Array) instead of being spread in N-rows (2D Array),
            a pair of tiles (a, b) form an inversion if a appears before b but a > b.
        Reference: https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
        """
        puzzle_1d = sum(self.puzzle, [])
        number_of_inversions = get_number_of_inversions(puzzle_1d) # Check Inversion
        # 1. If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
        if self.column % 2 == 1:
            print("N = ", self.column)
            print("Number of Inversions = ", number_of_inversions)
            # If number of inversions is even, this puzzle is solvable
            if number_of_inversions % 2 == 0:
                return True
            else:
                return False
        # 2. If N is even, puzzle instance is solvable if
        elif self.column % 2 == 0:
            blank_row, blank_column = self.find_blank()
            row_position_of_blank_from_botton = self.row - blank_row
            print("N = ", self.column)
            print("Position of Blank from botton = ", row_position_of_blank_from_botton)
            print("Number of Inversions = ", number_of_inversions)
            # the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) 
            if row_position_of_blank_from_botton % 2 == 0:
                # and number of inversions is odd.
                if number_of_inversions % 2 == 1:
                    return True
                else:
                    return False
            # the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.)
            else:
                # and number of inversions is even.
                if number_of_inversions % 2 == 0:
                    return True
                else:
                    return False
        else:
            return False

    def pretty_print(self):
        print("Row: {}\tColumn: {}\tSize: {}".format(str(self.row), str(self.column), str(self.size_of_puzzle)))
        for i in range(self.column + 1):
            print("=====", end='')
        print("=")
        for i in range(self.row):
            print("|", end='')
            for j in range(self.column):
                print("{0:^5}|".format(self.puzzle[i][j]), end='')
            print()
        for i in range(self.column + 1):
            print("=====", end='')
        print("=")



# Test Page
test_puzzle_1 = [6,13,7,10,8,9,11,_BLANK,15,2,12,5,14,3,1,4]
test_puzzle_2 = [3,9,1,15,14,11,4,6,13,_BLANK,10,12,2,7,8,5]
test_puzzle_3 = [[6,13,7,10], [8,9,11,_BLANK], [15,2,12,5], [14,3,1,4]]
puzzle = Puzzle.with_puzzle(test_puzzle_3)
puzzle.pretty_print()

