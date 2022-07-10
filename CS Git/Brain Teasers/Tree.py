

# File: Sugar.py
# Description: Help Alex identify if a graph is a tree.
# Student Name:Aayush  Singh
# Student EID:as92488
# Course Name: CS 313E
# Unique Number: 51120
import sys
# Feel free to define any helper functions, if necessary!
# Input: n - total number of vertices in graph, edges - set of all edge connections between vertices
# Output: true/false if graph is valid tree
def isTree(n, edges):
    lengthn = n-1
    if len(edges) != lengthn:
        return False
    else: 
        return True
        
# TAKE CAUTION TO EDIT BELOW


def main():
    n = int(sys.stdin.readline().strip())
    allEdges = []
    for line in sys.stdin:
        edge = list(map(int, line.split(" ")))
        allEdges.append(edge)
    print(isTree(n, allEdges))
if __name__ == "__main__":
    main()