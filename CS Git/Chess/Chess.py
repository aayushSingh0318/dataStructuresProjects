
#  Description: Counts the solutions to the famous queens problem. 
 

import sys

class Queens (object):
  queen_count = 0 
  def __init__ (self, n = 8):
    #self.solutions = solutions
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  '''def queen_count (self):
      queen_num = 0 
      for i in range(self.n): 
        for j in range(self.n):
            if self.board[i][j] != 'Q':
                pass
            else:
                queen_num = queen_num +1'''
                
  # do the recursive backtracking
  def recursive_solve (self, col=0):
    #self.counter = counter
    if (col == self.n):
      Queens.queen_count = Queens.queen_count + 1 #add to the counter 
      pass
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          self.recursive_solve(col + 1) #solves for column count after
            #return True
          self.board[i][col] = '*'
      

  # if the problem has a solution print the board
  def solve (self):
    for i in range (self.n):
      if (self.recursive_solve(i)):
        self.print_board()

def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)
  game.recursive_solve() #solves the chess board

  # place the queens on the board and count the solutions
  #game.solve()
  # print the number of solutions
  print(game.queen_count) #prints the count of the number of solution 
  
 
if __name__ == "__main__":
  main()
