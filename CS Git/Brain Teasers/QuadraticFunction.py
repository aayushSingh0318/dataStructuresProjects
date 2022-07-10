import math
from re import X
class QuadraticFunction (object):
    # Construct an object to represent an equation of the form f(x) = ax^2 + bx + c.
    # For simplicity, the a, b, and c coefficients will be given as ints.
    def __init__(self, a: int, b: int, c: int):
        self.a = a 
        self.b = b 
        self.c = c

    # Return a list containing the x-coordinates of the root(s) of this quadratic equation.
    # If there are multiple roots, return them sorted in ascending order.
    def roots(self):
        if self.a == 0 or self.b**2 -(4*self.a*self.c) < 0:
            return []
        x1 = (-(self.b) + math.sqrt(self.b**2 -(4*self.a*self.c)))/(2*self.a)
        x2 = (-(self.b) - math.sqrt(self.b**2 -(4*self.a*self.c)))/(2*self.a)
        if x1 == x2: 
            roots= [x1]
        else:
            roots = [x1, x2]
        roots.sort()
        return roots
        
    # Return the location of the vertex as a tuple (x,y).
    def vertex(self):
        tup = (-(self.b)/(2*self.a), self.evaluate(-(self.b)/(2*self.a)))
        return tup 
        
    # Return the y-coordinate of the graph at the given x-coordinate.
    def evaluate(self, x):
        return self.a * (x**2) + self.b * x + self.c
        
    # Return a string that represents this equation in the form: "f(x) = ax^2 + bx + c"
    # *If the coefficient for a term is 0, the term should not be included.
    def __str__(self):
        if self.a == 0:
            s = 'f(x) = '+ str(self.b)+'x + '+str(self.c)
        elif self.b == 0:
            s = 'f(x) = '+ str(self.a)+'x^2 + '+ str(self.c)
        elif self.c == 0:
            s = 'f(x) = '+ str(self.a)+'x^2 + '+str(self.b)+'x'
        else:
            s = 'f(x) = '+ str(self.a)+'x^2 + '+str(self.b)+'x + '+str(self.c)
            
        return s