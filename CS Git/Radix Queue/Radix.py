
from pdb import line_prefix
import queue
import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
    # dictionary of queues of numbers and letters
    queue_dict =  {'0' : Queue(), '1' : Queue(), '2' : Queue(), '3' : Queue(), '4' : Queue(), '5' : Queue(), '6' : Queue(), '7' : Queue(), '8' : Queue(), '9' : Queue(),
                   'a' : Queue(), 'b' : Queue(), 'c' : Queue(), 'd' : Queue(), 'e' : Queue(), 'f' : Queue(), 'g' : Queue(), 'h' : Queue(), 'i' : Queue(), 'j' : Queue(),
                   'k' : Queue(), 'l' : Queue(), 'm' : Queue(), 'm' : Queue(), 'n' : Queue(), 'o' : Queue(), 'p' : Queue(), 'q' : Queue(), 'r' : Queue(), 's' : Queue(),
                   't' : Queue(), 'u' : Queue(), 'v' : Queue(), 'w' : Queue(), 'x' : Queue(), 'y' : Queue(), 'z' : Queue(), '-' : Queue()}

  
    # radix_queue = Queue() #a queue is creaated
    # for line in a:
    #     radix_queue.enqueue(line) #enques the word in the specific line to the queue created
    
    longestlen = maximum_string_length(a)

    filling = []
    for space in a:
        while longestlen > len(space):
            space = space + '-' #fills all spaces to max number of characters with '-' 
        filling.append(space)
            
    sorted_string = filling
    index = longestlen
    for pos in range(index-1, -1, -1):
        for char_in in sorted_string:
            queue_dict[char_in[pos]].enqueue(char_in)

        in_order = []
        
        for key in sorted(queue_dict.keys()):
            pos = queue_dict[key]
            while pos.is_empty() == False:       
                in_order.append(pos.dequeue())
        
        sorted_string = in_order
    
    for pos in range(len(sorted_string)):
        sorted_string[pos] = sorted_string[pos].replace('-', '')

    return sorted_string

def maximum_string_length(a):
    maximumlen = 0
    for someString in a:
        if (len(someString) > maximumlen):
                maximumlen = len(someString)
    return maximumlen

    

'''  
    for i in range(maximumlen):
        while not radix_queue.is_empty():
            val = num = radix_queue.dequeue()
    
        if queue_dict[num[maximumlen-1]].enqueue(num):
        
            try:
                # print(num[index])
                queue_dict[num[maximumlen-1]].enqueue(num)
            except:
                # print(0)
                queue_dict['0'].enqueue(num)

        for i in queue_dict:
        for j in range(queue_dict[i].size()):
            radix_queue.enqueue(queue_dict[i].dequeue())

        index -= 1


    sort_list = []

    for item in radix_queue.queue:
        sort_list.append(item)

    return sort_list
'''
def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    
