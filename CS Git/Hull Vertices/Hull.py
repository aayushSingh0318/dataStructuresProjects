
import sys
import math

class Point (object):
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def dist (self, other):
		return math.hypot (self.x - other.x, self.y - other.y)

	def __str__ (self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

	def __equal__ (self, other):
		tolerance = 1.0e-8
		return (abs(self.x - other.x) < tolerance) and (abs(self.y - other.y) < tolerance)

	def __notequal__ (self, other):
		tolerance = 1.0e-8
		return (abs(self.x - other.x) >= tolerance) or (abs(self.y - other.y) >= tolerance)

	def __lessthan__ (self, other):
		tolerance = 1.0e-8
		if abs(self.x - other.x) < tolerance:
			if abs(self.y - other.y) < tolerance:
				return False
			else:
				return self.y < other.y
		return self.x < other.x

	def __lessequal__ (self, other):
		tolerance = 1.0e-8
		if abs(self.x - other.x) < tolerance:
			if abs(self.y - other.y) < tolerance:
				return True
			else:
				return self.y <= other.y
		return self.x <= other.x

	def __greaterthan__ (self, other):
		tolerance = 1.0e-8
		if abs(self.x - other.x) < tolerance:
			if abs(self.y - other.y) < tolerance:
				return False
			else:
				return self.y > other.y
		return self.x > other.x

	def __greaterequal__ (self, other):
		tolerance = 1.0e-8
		if abs(self.x - other.x) < tolerance:
			if abs(self.y - other.y) < tolerance:
				return True
			else:
				return self.y >= other.y
		return self.x >= other.x


def matrix(p, q, r):
   return [[1,p.x,p.y],[1,q.x,q.y],[1,r.x,r.y]]
def matrix_det():  
    val1 = matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[1][2] * matrix[2][1])
    val2 = matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[1][2] * matrix[2][0])
    val3 = matrix[0][2] * (matrix[1][0]*matrix[2][1] - matrix[1][1]* matrix[2][0])
    return val1 - val2 + val3 
     
def hull():     
# 1.  Sort the points by x-coordinates resulting in a sorted sequence
#     p_1 ... p_n.

    sorted_x = sorted(points , key=lambda k: [k[1], k[0]])
    # 2.  Create an empty list upper_hull that will store the vertices
    #     in the upper hull.

    upper_hull = []

    # 3.  Append the first two points p_1 and p_2 in order into the upper_hull.
    upper_hull.append(sorted_x[0])
    upper_hull.append(sorted_x[1])
    # 4.  For i going from 3 to n 
    for i in range(2,len(sorted_x)):
        upper_hull.append(sorted_x[i])

    # 5.    Append p_i to upper_hull.

    # 6.    While upper_hull contains three or more points and the last three
    #       points in upper_hull do not make a right turn do (refer to the
    # 	  notes below on determinants for right and left interpretations)
        while (matrix_det(upper_hull[-1],upper_hull[-2],upper_hull[-3]) < 0) and (len(upper_hull) >=3) :
            upper_hull.pop(-2)

    # 7.    Delete the middle of the last three points from upper_hull

    # 8.  Create an empty list lower_hull that will store the vertices
    #     in the lower hull.
    lower_hull = []
    # 9.  Append the last two points p_n and p_n-1 in order into lower_hull with
    #     p_n as the first point.
    lower_hull.append(sorted_x[-1])
    lower_hull.append(sorted_x[-2])

    # 10. For i going from n - 2 downto 1
    for i in range(len(sorted_x)-3,-1,-1):
        lower_hull.append(sorted_x[i])
        while (len(lower_hull) >= 3) and (matrix_det(lower_hull[-1],lower_hull[-2],lower_hull[-3]) < 0):
            lower_hull.pop(-2)

    lower_hull.pop(0)
    lower_hull.pop(-1)
    upper_hull.extend(lower_hull)


            
        
    # 11.   Append p_i to lower_hull

    # 12.   While lower_hull contains three or more points and the last three
    #       points in the lower_hull do not make a right turn do
            

    # 13.     Delete the middle of the last three points from lower_hull

    # 14. Remove the first and last points for lower_hull to avoid duplication
    #     with points in the upper hull.

    # 15. Append the points in the lower_hull to the points in the upper_hull 
    #     and call those points the convex_hull

    # 16. Return the convex_hull.  
    return upper_hull

def read_input():
    points = []
    sys.stdin = open('hull.in', 'r') #test the code
    num_points = sys.stdin.readline()
    for l in range(num_points):
        line = sys.stdin.readline().strip().split() 
        newpoint = Point(line[0],line[1])
        points.append(newpoint)
    
