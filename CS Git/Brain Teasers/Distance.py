# File: RiverFlow.py

# Description: Determine if a river can flow off the map given starting point.

# Student Name: Aayush Singh

# Student EID: as92488

# Course Name: CS 313E

# Unique Number: 51120

import sys


# Input: two strings:
# Output: the edit distance between the two input strings
def edit_distance(str1, str2):
    """STUDENT TODO"""

    if len(str2) == 0:
        return len(str1) 
    if len(str1) == 0:
        return len(str2)
    
    length1 = len(str1)-1
    length2 = len(str2)-1
    if str1[length1] != str2[length2]:
        edited = min(edit_distance(str1, str2[:-1]), edit_distance(str1[:-1], str2), edit_distance(str1[:-1], str2[:-1]))
        return 1 + edited
    else:
        return edit_distance(str1[:-1], str2[:-1])
    


# TAKE CAUTION TO EDIT BELOW
if __name__ == "__main__":
    str1 = sys.stdin.readline()[:-1]
    str2 = sys.stdin.readline()[:-1]
    print(edit_distance(str1, str2))
