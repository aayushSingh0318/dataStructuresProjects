#  File: WordSearch.py

#  Description: This code inputs the word_grid text file and splits it into a word grid and a word list. 
# It then iterates through the word list and the word grid and returns the coordinates where the word is found. 

#  Student Name: Eesha Patel

#  Student UT EID: ep26454

#  Partner Name: Aayush Singh

#  Partner UT EID: as92488

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 1/21/22

#  Date Last Modified: 1/27/22


#need to separate the word search grid from the words
#need to figure out how to go through and identify the lines 

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
    word_grid = []
    word_list = []

    size = int(sys.stdin.readline())
    sys.stdin.readline()

    for line in range(size):
      row = sys.stdin.readline()
      row = row.strip()
      row = row.replace(' ', '')
      word_grid += [row]

    sys.stdin.readline()
    wordnum = int(sys.stdin.readline())

    for line in range(wordnum):
      word = sys.stdin.readline()
      word = word.strip()
      word_list.append(word)

    return word_grid, word_list

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid


'''
  left(grid, word, row, col)

  right(grid, word, row, col)

  up(grid, word, row, col)

  down(grid, word, row, col)

  diag_up_left(grid, word, row, col)
  diag_up_right(grid, word, row, col)
  diag_down_left(grid, word, row, col)
  diag_down_right(grid, word, row, col)
'''

"""
d u r
h x d
a n b
t r s
z y d
"""

def search(grid, word, row, col):

  # NORTH
  currRow = row
  wordSoFar = ""
  while currRow >= 0:
    wordSoFar += grid[currRow][col]
    currRow -= 1
    if wordSoFar == word:
      return True

  # SOUTH
  currRow = row
  wordSoFar = ""
  while currRow < len(grid):
    wordSoFar += grid[currRow][col]
    currRow += 1
    if wordSoFar == word:
      return True

  # EAST
  currCol = col
  wordSoFar = ""
  while currCol < len(grid):
    wordSoFar += grid[row][currCol]
    currCol += 1
    if wordSoFar == word:
      return True

  # WEST
  currCol = col
  wordSoFar = ""
  while currCol >= 0:
    wordSoFar += grid[row][currCol]
    currCol -= 1
    if wordSoFar == word:
      return True
  
  # NORTHEAST
  currCol = col
  currRow = row
  wordSoFar = ""
  while currRow >= 0 and currCol < len(grid):
    wordSoFar += grid[currRow][currCol]
    currRow -= 1
    currCol += 1
    if wordSoFar == word:
      return True

  # NORTHWEST
  currCol = col
  currRow = row
  wordSoFar = ""
  while currRow >= 0 and currCol < len(grid):
    wordSoFar += grid[currRow][currCol]
    currRow -= 1
    currCol -= 1
    if wordSoFar == word:
      return True

  # SOUTHEAST
  currCol = col
  currRow = row
  wordSoFar = ""
  while currRow < len(grid) and currCol < len(grid):
    wordSoFar += grid[currRow][currCol]
    currRow += 1
    currCol += 1
    if wordSoFar == word:
      return True

  # SOUTHWEST
  currCol = col
  currRow = row
  wordSoFar = ""
  while currRow < len(grid) and currCol < len(grid):
    wordSoFar += grid[currRow][currCol]
    currRow += 1
    currCol -= 1
    if wordSoFar == word:
      return True

  return False


  #print(grid, word, row, col)
  #search left
  for letter in range(str(word)):
    print(word[letter])
    # if grid[row][col] == word[letter]:
    #   col -= 1
  #search right 


def find_word (grid, word): 
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] == word[0]:
        if search(grid, word, row, col):
          return (row + 1, col + 1)
  return (0,0)

def main():

  grid, word_list = read_input()

  # find each word and print its location
  for word in word_list:
    location = find_word (grid, word)
    print(word + ": " + str(location))

if __name__ == "__main__":
  main()