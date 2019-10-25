"""
This Module is about building Pattern Database.
"""

from puzzle import BLANK
from itertools import permutations # For generating
import time

"""
The 5-5-5 partition is this
        pattern A                  pattern B                  pattern C
=========================  =========================  =========================
|  1  |  2  |  3  |  4  |  |  *  |  *  |  *  |  *  |  |  *  |  *  |  *  |  *  |
|  *  |  *  |  7  |  *  |  |  5  |  6  |  *  |  *  |  |  *  |  *  |  *  |  8  |
|  *  |  *  |  *  |  *  |  |  9  | 10  |  *  |  *  |  |  *  |  *  | 11  | 12  |
|  *  |  *  |  *  |  *  |  | 13  |  *  |  *  |  *  |  |  *  | 14  | 15  |  *  |
=========================  =========================  =========================
"""
PATTERN_5_5_5 = [[1, 2, 3, 4, BLANK, BLANK, 7, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK, BLANK, 5, 6, BLANK, BLANK, 9, 10, BLANK, BLANK, 13, BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, 8, BLANK, BLANK, 11, 12, BLANK, 14, 15, BLANK]]
"""
The 6-6-3 partition is this
        pattern A                  pattern B                  pattern C
=========================  =========================  =========================
|  1  |  *  |  *  |  *  |  |  *  |  *  |  *  |  *  |  |  *  |  2  |  3  |  4  |
|  5  |  6  |  *  |  *  |  |  *  |  *  |  7  |  8  |  |  *  |  *  |  *  |  *  |
|  9  | 10  |  *  |  *  |  |  *  |  *  | 11  | 12  |  |  *  |  *  |  *  |  *  |
| 13  |  *  |  *  |  *  |  |  *  | 14  | 15  |  *  |  |  *  |  *  |  *  |  *  |
=========================  =========================  =========================
"""
PATTERN_6_6_3 = [[1, BLANK, BLANK, BLANK, 5, 6, BLANK, BLANK, 9, 10, BLANK, BLANK, 13, BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, 7, 8, BLANK, BLANK, 11, 12, BLANK, 14, 15, BLANK], [BLANK, 2, 3, 4, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK]]
"""
The 7-8 partition is this
        pattern A                  pattern B
=========================  =========================
|  1  |  2  |  3  |  4  |  |  *  |  *  |  *  |  *  |
|  5  |  6  |  7  |  8  |  |  *  |  *  |  *  |  *  |
|  *  |  *  |  *  |  *  |  |  9  | 10  | 11  | 12  |
|  *  |  *  |  *  |  *  |  | 13  | 14  | 15  |  *  |
=========================  =========================
"""
PATTERN_7_8 = [[1, 2, 3, 4, 5, 6, 7, 8, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, 9, 10, 11, 12, 13, 14, 15, BLANK]]

def building_database_5_5_5():
    # Working
    return 0