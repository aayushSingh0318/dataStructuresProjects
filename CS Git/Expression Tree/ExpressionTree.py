#  File: ExpressionTree.py

#  Description: This is an expression tree. 


import sys

##operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lChild = None
        self.rChild = None
    


class Tree (object):
    def __init__ (self):
        self.root = Node(None)
        self.ops = ['+', '-', '*', '/', '//', '%', '**'] #operators

    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        #print(expr)
        newStack = Stack () #create a stack 
        newNode = self.root
        
        for pos in expr.split():
            
            if pos == '(':
                newNode.lChild = Node(None)
                newStack.push(newNode) 
                newNode = newNode.lChild
            elif pos in self.ops:
                newNode.data = pos
                newStack.push(newNode)
                newNode.rChild = Node(None)
                newNode = newNode.rChild
            elif pos == ')':
                if not newStack.is_empty():
                    newNode = newStack.pop()
            else:
                try:
                    newNode.data = int(pos)
                except:
                    newNode.data = float(pos)

                '''if pos.isnumeric():
                    newNode.data = int(pos)
                else:
                    newNode.data = float(pos)'''

                newNode = newStack.pop()
                    
    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):

        if aNode.data in self.ops:
            eval = self.evaluate(aNode.lChild),self.evaluate(aNode.rChild),aNode.data
            #print(eval)
            #print('eval')
            return self.solver(self.evaluate(aNode.lChild),self.evaluate(aNode.rChild),aNode.data)
        else:
            #print(aNode.data)
            #print('data')
            return aNode.data
        
    def solver(self,item1, item2, operation):
        if operation =='-':
            return float(item1 - item2)
        if operation =='+':
            return float(item1 + item2)
        if operation =='/':
            return float(item1 / item2)
        if operation =='//':
            return float(item1 // item2)
        if operation =='*':
            return float(item1 * item2)
        if operation =='**':
            return float(item1 ** item2)
        if operation =='%':
            return float(item1 % item2)
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        if (aNode == None):
            return ''
        else:
            #if aNode.data != None:
            empty = str(aNode.data) + ' '
            empty = empty + self.pre_order(aNode.lChild)
            empty = empty + self.pre_order(aNode.rChild)
            return empty
        
    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        if (aNode != None):
            empty = ''
            empty =  empty + self.post_order(aNode.lChild)
            empty = empty + self.post_order(aNode.rChild)
            if aNode.data == None:
                pass
            else:
                empty = empty + str(aNode.data) + ' '
            return empty
        return ''

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
