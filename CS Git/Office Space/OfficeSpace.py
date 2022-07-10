#  File: OfficeSpace.py

#  Description: We satisified the required methods.

#  Student Name:Aayush Singh

#  Student UT EID:as92488

#  Partner Name:Danny Xie

#  Partner UT EID:dax56

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/11/2022

#  Date Last Modified: 2/11/2022

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
from cmath import rect
import sys
def area (rect):
    x_dist = abs(rect[2] - rect[0])
    y_dist = abs(rect[3] - rect[1])
    area = x_dist * y_dist
    return area

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
  
  xmax = max(rect1[0], rect2[0])
  ymax = max(rect1[1], rect2[1])
  xmin = min(rect1[2], rect2[2])
  ymin = min(rect1[3], rect2[3])
  if ((xmin - xmax) * (ymin - ymax) != 0):
        return (xmax, ymax, xmin, ymin)
  else:
		    return (0, 0, 0, 0)
          
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
  '''office_space = []
  alternate_grid = []
  for i in range(bldg[0]):
        for j in range(bldg[1]):
              alternate_grid.append(0)
        office_space.append(alternate_grid)'''
        
  counter = 0       
  for i in range(len(bldg)):
      for j in range(len(bldg[i])): 
          if bldg[i][j] == 0:
                counter += 1
  return counter 
          
          
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
  counter = 0       
  for i in range(len(bldg)):
      for j in range(len(bldg[i])):
          if bldg[i][j] >= 2:
                counter += 1
  return counter 
      

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    [x1,y1,x2,y2] = rect
    total = area(rect)
    contested_space = 0       
    for i in range(y1,y2):
        for j in range(x1,x2):
            if bldg[i][j] >= 2:
                  contested_space += 1
    return total - contested_space
            
# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    bldg = [[0]*office[2] for i in range(office[3])]
    for name, x1, y1, x2, y2 in cubicles:
          for i in range(y1, y2):
                for j in range(x1, x2):
                      bldg[i][j] += 1
    return bldg
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed"

def main():
    # read the data
    #blank = sys.stdin.readline()
    [officespacex, officespacey] = list(map(int,sys.stdin.readline().strip().split()))
    total_area = officespacex * officespacey 
    num_employees = int(sys.stdin.readline())
    employee_points = []
    for num in range(num_employees):
        employee_line = sys.stdin.readline().strip().split() 
        name = employee_line[0]
        x1 = int(employee_line[1])
        y1 = int(employee_line[2])
        x2 = int(employee_line[3])
        y2 = int(employee_line[4])
        
        employee_points.append((name,x1,y1,x2,y2))
    office = (0,0, officespacex, officespacey)
    bldg = request_space(office, employee_points)
        
    
    print('Total' ,area((0, 0, officespacex, officespacey)))
    print('Unallocated',unallocated_space(bldg))
    print('Contested',contested_space(bldg))
    for name, x1, y1, x2, y2 in employee_points:
        print(name, uncontested_space(bldg,(x1, y1, x2, y2)))
    
  # compute the total unallocated space

  # compute the total contested space

  # compute the uncontested space that each employee gets

if __name__ == "__main__":
  main()