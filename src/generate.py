""" This module is about Generating all solvable Puzzles

- Generate all solvable puzzles.
- Write all possible (and solvable) Puzzles on Database
- Maria DB is the Database system that we use.
"""

from puzzle import is_solvable, BLANK
from itertools import permutations # For generating
import threading # For fast
import multiprocessing # For fast
import numpy as np
import time

def return_solvable(puzzle):
    if is_solvable(puzzle):
        return str(puzzle)

def number_of_permutations(number_of_item = 16):
    return_value = 1
    for i in range(2, (number_of_item + 1)):
        return_value = return_value * i
    return return_value

def write_on_database(something_to_write, database_name = "Database.txt"):
    dimension_of_something_to_write = len(np.shape(something_to_write))
    #print("Dimension : ", dimension_of_something_to_write)
    something_to_write = list(something_to_write)
    with open(database_name, 'a') as database:
        if dimension_of_something_to_write == 1:
            database.write(str(something_to_write))
            database.write("\n")
        elif dimension_of_something_to_write == 2:
            for item in something_to_write:
                database.write(str(list(item))+"\n")

# Total Execution time (3x3): 16.109595775604248 seconds
# Writing time: 0.7217490673065186 seconds
# Calc time: 15.402843475341797 seconds
# This means need to cut off the time for calculate.
def generate_all_solvable_square_puzzles(row = 4, column = 4, cpu_core = 2):
    estimated_number_of_solvable_states = number_of_permutations(row * column) / 2
    ONE_PERCENT = int(estimated_number_of_solvable_states / 100) # the one percent of working
    percent_iteration = 0.5
    print(estimated_number_of_solvable_states)
    count_permutations = 0
    number_array = [None] * (row * column)
    for i in range(row * column):
        number_array[i] = i
    number_array[0] = BLANK
    _database_name = "All_Solvable_Puzzle_" + str(row) + "x" + str(column) + "_thread.txt"
    _write_things = ""
    write_time = 0

    pool = multiprocessing.Pool(8)
    with open(_database_name, 'a') as database:
        for possible_and_solvable_state in pool.imap_unordered(return_solvable, permutations(number_array), chunksize = 150):
            start_time = time.time()
            if possible_and_solvable_state is not None:
                database.write(possible_and_solvable_state + "\n")
                count_permutations = count_permutations + 1
            write_time = write_time + (time.time() - start_time)
            if count_permutations == ONE_PERCENT * percent_iteration:
                print(percent_iteration, "% is done")
                percent_iteration = percent_iteration + 0.5

    print("Generating all solvable and possible permutations of puzzles!")
    print("The number of all Possible and Solvable puzzle is ", count_permutations)
    return write_time

if __name__=='__main__':
    start_time = time.time()
    writing_time = generate_all_solvable_square_puzzles(4, 4, 4)
    print("Execution time: %s seconds" % (time.time() - start_time))
    print("Writing time: %s seconds" % writing_time)
    print("Calc time: %s seconds" % (time.time() - start_time - writing_time))
