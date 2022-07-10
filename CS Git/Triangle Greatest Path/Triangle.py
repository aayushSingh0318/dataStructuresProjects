
#  File: Triangle.py

#  Description: Using Recursion and different methods of solving, we are able to traverse through a triaangle (2D list) and find the path with the greaates sum of values. 

#  Student Name: Aayush Singh

#  Student UT EID: as92488

#  Partner Name: Danny Xie

#  Partner UT EID: dax56

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/4/2022

#  Date Last Modified: 3/4/2022


import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
# make list that stores every possible sum, go though every possible sum recursive
def brute_force (grid):
  
  all_paths = [] #stores all path sums 
  
  exhaustive_recursive_search(grid, 0, 0, 0, all_paths) #calls recursive helper
 
  greatest_path = max(all_paths) #max value in list 
  return greatest_path

def exhaustive_recursive_search(grid, column_count, row_count, sum, all_paths):
    if row_count >= (len(grid)): #base case
        all_paths.append(sum) #add a path to list 
    else:
        sum += grid[row_count][column_count]
        exhaustive_recursive_search(grid, column_count, row_count+1 , sum, all_paths) or exhaustive_recursive_search(grid, column_count + 1, row_count + 1, sum, all_paths) #no return bc sum is appended to all_path[]

# returns the greatest path sum using greedy approach
# each row you pick with one is bigger 
def greedy (grid):
    sum = 0
    column_count = 0 
    #sum = grid[0][0] #each sum starts with beginning value of the top of the triangle
    size = range(len(grid) - 1)
    
    for pos in size:
      sum += grid[pos][column_count] #the current position in the triangle is added to sum
      if grid[pos + 1][column_count] <= grid[pos + 1][column_count + 1]:
        column_count += 1 #move forward
      else:
        pass
    sum += grid[pos + 1][column_count]
    return sum


# returns the greatest path sum using divide and conquer (recursive) approach
# recursive 
# each num is on top of two triangles, there are 4 possible sums
# find max of the four sums and pick it for row 2 
def divide_conquer (grid):    
  all_paths = [] #list of sum of all paths
  sum = 0 #current sum
  divide_recursive_conquer(grid, 0, all_paths)
  maximum_path = max(all_paths)
  return maximum_path #return max

def divide_recursive_conquer(grid, sum, all_paths):
  if len(grid) == 1: #base case
    all_paths.append(grid[0][0] + sum) #append sum current value to first digit
  else:
    left_tri = [] #create two lists representing the two triangles created
    right_tri = []
    for line in grid[1:len(grid)]:
          left_tri.append(line[1:len(grid)])
          right_tri.append(line[0:-1])
    sum = sum + grid[0][0]
    return divide_recursive_conquer(left_tri, sum, all_paths) or divide_recursive_conquer(right_tri, sum, all_paths) 

# returns the greatest path sum and the new grid using dynamic programming
# not recursive
# start from bottom and go up
# compare which sum is greatest from bottom up,
# replace with sum, and continue going up
def dynamic_prog (grid):
  for i in range(len(grid) - 2, -1, -1):
      if i == len(grid) - 1:
          pass
      for j in range(len(grid) - 1):
          if grid[i + 1][j] >= grid[i + 1][j + 1]:
              grid[i][j] += grid[i + 1][j]
          elif grid[i + 1][j + 1] >= grid[i + 1][j]:
              grid[i][j] += grid[i + 1][j + 1]
  return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()

