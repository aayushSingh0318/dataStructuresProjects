#  File: WordSearch.py

#  Description:

#  Student Name: Aayush Singh 

#  Student UT EID: as92488 

#  Partner Name: Eesha Patel 

#  Partner UT EID: ep26454

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 1/21/2022

#  Date Last Modified: 

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ():
  word_grid = []
  word_list = []
  
  sys.stdin = open('word_grid.in', 'r') #test the code
  size = sys.stdin.readline()
  #print(size) #14 as a str
  n = int(size) #gets size of grid
  #print(n)
  line = sys.stdin.readline() #accounts for first blank line
  
  for i in range(n): #loop will iterate
        line = sys.stdin.readline()   
        line = line.strip()
        line = line.replace(' ', '')
        word_grid.append(line) #try extend
        
          
  #print(word_grid)
  
  line = sys.stdin.readline() #accounts for second blank line
  
  wordnum = sys.stdin.readline()
  m = int(wordnum) #gets number of words
  counter = 0 #reset counter
  
  for j in range(m):
        line = sys.stdin.readline()
        line = line.replace('\n', '')
        word_list.append(line)
        
  #print(word_list)
  return word_grid, word_list

    

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid

def find_word (grid, word):
  

def find_word (grid = read_input()[0], word = read_input()[1]): 
  #for each word in the word list
  word_and_loc = []
  length = len(grid)
  for row in range(length):
    for col in range(length):
      #print(grid[row][col], end = " ")
      if word[0] == grid[row][col]:
        search_word(grid, word, row, col)
      else: 
        break
              
def search_word(grid, word, row, col):
  #search left
  for letter in range(str(word)):
    if grid[row][col] == word[letter]:
      col -= 1
  #right
  for letter in range(word):
      if grid[row][col] == word[letter]:
        col += 1
      else:
        break
  for x in grid:
    col = 1
    string = ''
    while col < len(grid):
      string += grid[x][col]
      col += 1 
      if str == word:
        return True
      else:
        continue
                  

              
        
        
        

        ''' #if the letter is the same as the first letter in the word
      if word_x = 
		  if word_grid[grid_x, grid_y] == word[0]:
        #go through the surrounding letters and see if they match up
        left()
        right()
        up()
        down()
        diag_up_left()
            
    
def left(grid, word, n, start_cord):
    dx = -1
    dy = 0
    
  if word[n] == grid[i][k-1] #k = word in word_list
def right(grid, word, n):
  
def up(grid, word, n):

def down(grid, word, n):

def diag_up_left(grid, word, n):

def diag_up_right(grid, word, n):

def diag_down_left(grid, word, n):

def diag_down_right(grid, word, n):'''
      


# #def find_word_helper(grid, word, index, coord):
#   #when your index is the size of word:
#     return True
#   if grid[coord] == word[index]:
        
#         up, left right -> find_word_helper(grid, word, index+1, new_coord, start_coord)

def main():
  # read the input file from stdin
  
  
  # line = sys.stdin.readline()
  # print(line)
  # n = int(line) #gets number of words or size of grid
  # print(n)
  # line = sys.stdin.readline() #accounts for second blank line
  
  #read_input()
  word_grid, word_list = read_input()

  # find each word and print its location
  for word in word_list:
    location = find_word (word_grid, word)
	  #print(word + ": " + str(location))
 

if __name__ == "__main__":
  main()
