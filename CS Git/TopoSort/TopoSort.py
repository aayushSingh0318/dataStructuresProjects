

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []
    
  def within(self,label):
    list = []
    while (not self.is_empty()):
      list.append(self.pop())
      list.reverse()
    for char in list:
      self.push(char)
    if (label in list):
      return True
    return False

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))

  


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))

  def first(self):
      return self.queue[0]

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)


class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (self.has_vertex (label)):

        self.Vertices.append (Vertex (label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append(0)

    # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not(self.Vertices[i]).was_visited()):
        return i
    return -1

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).was_visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).was_visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).was_visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
    q = Queue() #create a queue
    self.Vertices[v].was_visited = True #mark the vertex as visited
    print(self.Vertices[v])
    q.enqueue(v) #queue the vertex
    while q.is_empty() == False: #while the queue is not empty
      u = self.get_adj_unvisited_vertex(q.first()) #get an adjacent unvisited vertex
      if u == -1:
        u = q.dequeue() #dequeue u
      else:
        self.Vertices[u].was_visited = True
        print(self.Vertices[u]) #after set to true, print that vertex
        q.enqueue(u) #queue next
        
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).was_visited = False
  
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    from_idx = self.get_index(fromVertexLabel) #gets the starting index
    to_idx= self.get_index(toVertexLabel) #gets the ending index
    self.adjMat[from_idx][to_idx] = 0 #sets [start][end] equal to 0 in the adj matrix
    if self.adjMat[to_idx][from_idx] != 0: #if not equal to zero then make it equal to zero
      self.adjMat[to_idx][from_idx] = 0

  def delete_vertex (self, vertexLabel):
    index = self.get_index(vertexLabel)
    del(self.Vertices[index]) #delete the vertex
    del(self.adjMat[index]) #delete the vertex in the adj matrix
    for i in range (len(self.Vertices)):
      del(self.adjMat[i][index]) #adjusts the adj matrix

  def has_cycle(self):
      nVert = len(self.Vertices) #length of number of vertices
      if nVert > 0:
          s = Stack() #create a stack
          idx = 0 #set the index of the vertex to zero
          self.Vertices[idx].was_visited = True
          s.push(idx) #push on to the stack
          while s.is_empty() == False:
              next = self.get_adj_unvisited_vertex(s.peek()) 
              if next == -1:
                  next = s.pop() #pop if -1
              else:
                  self.Vertices[next].was_visited = True
                  s.push(next) #push the next value in the stack
                  for i in range(nVert):
                      if(self.adjMat[next][i] != 0) and (i in s.stack):
                              return True 
          return False
      else:
        return False


  def toposort (self):
    q = Queue()
    nVert = len(self.Vertices)
    in_degrees = {} #first vertex has to have an in-degree of zero; create a dictionary to keep track of each vertex and its in-degree
    for v in range(nVert):
        counter = 0
        for i in range(nVert):
            if self.adjMat[i][v] > 0: #if not zero in the adj mat
                counter += 1 #add one to counter
        in_degrees[self.Vertices[v]] = counter #set in-degree equal to the counter
    while len(in_degrees) > 0: #loop while the in degree is greater than zero
        vertices_list = [] #create a list of vertices
        for e in in_degrees:
            if in_degrees[e] == 0: #if equal to zero then add to the list of vertices
                vertices_list.append(e)
        queue_list = [] #create a queue list
        for e in vertices_list:
            idx = self.Vertices.index(e) #get the index of each edge (e) in vertice list
            for v in range(nVert):
                    if self.adjMat[idx][v] > 0: #not zero in adj mat
                        in_degrees[self.Vertices[v]] -= 1
            in_degrees.pop(e) #pop zero  
            queue_list.append(e.get_label) #append the edge
        queue_list.sort() #make the queue list alphabetical
        for i in queue_list: #queue each e in vertices list
            q.enqueue(i) 
    sorted = []
    while q.is_empty() == False:
        x = q.dequeue() #dequeue edge
        sorted.append(x)
    return sorted

def main():
  # create the Graph object
  cities = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    city = line.strip()
    cities.add_vertex (city)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)

  # read each edge and place it in the adjacency matrix
  for i in range (num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  # read the starting vertex for dfs and bfs
  line = sys.stdin.readline()
  start_vertex = line.strip()

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)

  # do the depth first search
  print ("Depth First Search")
  cities.dfs (start_index)
  print ()
    
if __name__ == "__main__":
  main()

