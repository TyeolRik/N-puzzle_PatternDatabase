""" This module is about Puzzle Class

- Generate Puzzle by getting user's input (size of puzzle)
- Default Puzzle is 15-puzzle.
- Make all possible puzzles.
- Move blank.
"""

import math
import random
import numpy as np

BLANK = '*'

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
        if puzzle_1d_array[i] != BLANK:
            for j in range(i, len(puzzle_1d_array)):
                if puzzle_1d_array[j] != BLANK:
                    # print(puzzle_1d_array[i], " compare ", puzzle_1d_array[j])
                    if puzzle_1d_array[i] > puzzle_1d_array[j]:
                        number_of_inversions = number_of_inversions + 1
    return number_of_inversions

def is_solvable(puzzle):
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

    Args:
        puzzle: 1-dimension or 2-dimension list. no 4
    Reference: https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
    """
    dimension = len(np.shape(puzzle))
    if dimension == 2:
        puzzle = sum(puzzle, [])
    elif dimension >= 3:
        print("Testing Puzzle's dimension is ", dimension, " >= 3. Please check puzzle data again.")
        return False
    row = column = int(math.sqrt(len(puzzle)))
    number_of_inversions = get_number_of_inversions(puzzle) # Check Inversion
    # 1. If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
    if column % 2 == 1:
        # print("N = ", column)
        # print("Number of Inversions = ", number_of_inversions)
        # If number of inversions is even, this puzzle is solvable
        if number_of_inversions % 2 == 0:
            return True
        else:
            return False
        # 2. If N is even, puzzle instance is solvable if
    elif column % 2 == 0:
        blank_row = int(puzzle.index(BLANK) / row)
        row_position_of_blank_from_botton = row - blank_row
        # print("N = ", column)
        # print("Position of Blank from botton = ", row_position_of_blank_from_botton)
        # print("Number of Inversions = ", number_of_inversions)
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

class Puzzle:
    row = 4
    column = 4
    size_of_puzzle = 16
    puzzle = []

    def __init__(self, number_of_row = 4, number_of_column = 4):
        """
        Args:
            number_of_row: The Number of Row.
            number_of_column: The Number of Column.
        Examples:
            >>> # In this case, there is no real puzzle data
            >>> test_puzzle = Puzzle(4, 4)
            >>> test_puzzle = Puzzle(4, 4).with_square_number(16)

            >>> # In this case, puzzle is in random state
            >>> test_puzzle = Puzzle(4, 4)
            >>> test_puzzle.set_puzzle_random()
            >>> test_puzzle.pretty_print()
            >>> Row: 4  Column: 4       Size: 16
                ==========================
                |  9  | 14  |  8  |  1  |
                |  4  |  3  |  5  |  *  |
                |  7  | 12  |  2  |  6  |
                | 10  | 13  | 11  | 15  |
                ==========================
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

    def set_puzzle(self, puzzle_1_dimension):
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
    
    def set_puzzle_random(self):
        """
        Set puzzle random

        Example:
            >>> test_puzzle = Puzzle(4, 4)
            >>> test_puzzle.set_puzzle_random()
        """
        puzzle_1_dimension = [i for i in range(self.size_of_puzzle)]
        puzzle_1_dimension[0] = BLANK
        random.shuffle(puzzle_1_dimension)
        while (is_solvable(puzzle_1_dimension) == False):
            random.shuffle(puzzle_1_dimension)
        self.set_puzzle(puzzle_1_dimension)

    def make_puzzle(self):
        self.puzzle = [[i*self.column+j+1 for j in range(self.column)] for i in range(self.row)]
        self.puzzle[self.row - 1][self.column - 1] = BLANK # Last Index should be blank(== BLANK like `*`)
        return self

    def shuffle(self):

        return self

    def move_tile_with_number(self, to):
        """
        Args:
            to: This argument should be "Near tile" from blank. Distance should be 1

        Example:
            >>> puzzle.move_tile_with_number(20).pretty_print()
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
            >>> puzzle.move_tile_with_direction("up").pretty_print()
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
                if self.puzzle[i][j] == BLANK:
                    return i, j
    
    def find_number(self, number_or_asterisk_to_find):
        """
        Args:
            number_or_asterisk_to_find: ex) 0, 1, 2, ..., BLANK
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
            # print("N = ", self.column)
            # print("Number of Inversions = ", number_of_inversions)
            # If number of inversions is even, this puzzle is solvable
            if number_of_inversions % 2 == 0:
                return True
            else:
                return False
        # 2. If N is even, puzzle instance is solvable if
        elif self.column % 2 == 0:
            blank_row, blank_column = self.find_blank()
            row_position_of_blank_from_botton = self.row - blank_row
            # print("N = ", self.column)
            # print("Position of Blank from botton = ", row_position_of_blank_from_botton)
            # print("Number of Inversions = ", number_of_inversions)
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


"""
# Test Page
test_puzzle_1 = [6,13,7,10,8,9,11,BLANK,15,2,12,5,14,3,1,4]
test_puzzle_2 = [3,9,1,15,14,11,4,6,13,BLANK,10,12,2,7,8,5]
test_puzzle_3 = [[6,13,7,10], [8,9,11,BLANK], [15,2,12,5], [14,3,1,4]]
test_puzzle_4 = [10, 4, 1, 9, 12, 5, 13, BLANK, 6, 14, 2, 11, 3, 7, 8, 15] # unsolvable
test_made = [BLANK, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14]
puzzle = Puzzle.with_puzzle(test_made)
puzzle.pretty_print()
print(puzzle.is_solvable())
test_puzzle = Puzzle(4, 4)
test_puzzle.set_puzzle_random()
test_puzzle.pretty_print()
print(test_puzzle.is_solvable())
"""