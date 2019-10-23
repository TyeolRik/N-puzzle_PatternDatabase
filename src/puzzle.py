""" This module is about Puzzle Class

- Generate Puzzle by getting user's input (size of puzzle)
- Default Puzzle is 15-puzzle.
- Make all possible puzzles.
- Move blank.
"""

import math

class Puzzle:
    row = 4
    column = 4
    size_of_puzzle = 16
    puzzle = []

    def __init__(self, number_of_row, number_of_column):
        self.row = number_of_row
        self.column = number_of_column
        self.size_of_puzzle = number_of_row * number_of_column

    @classmethod
    def withSquareNumber(cls, square_number):
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

    def make_puzzle(self):
        self.puzzle = [[0 for j in range(self.column)] for i in range(self.row)]
        return self
    def pretty_print(self):
        print("Row: {}\tColumn: {}\tSize: {}".format(str(self.row), str(self.column), str(self.size_of_puzzle)))
        print("=========================")
        for i in range(self.row):
            print("|", end='')
            for j in range(self.column):
                print("{0:^5d}|".format(self.puzzle[i][j]), end='')
            print()
        print("=========================")



puzzle = Puzzle.withSquareNumber(16)
puzzle.make_puzzle().pretty_print()

