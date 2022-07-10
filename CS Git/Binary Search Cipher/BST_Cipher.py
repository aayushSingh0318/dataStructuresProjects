#  File: BST_Cipher.py

#  Description: This is a BST cipher

#  Student Name: Aayush Singh

#  Student UT EID: as92488

#  Partner Name: Danny Xie

#  Partner UT EID: dax56

#  Course Name: CS 313E

#  Unique Number: 51220

#  Date Created: 4/18/22

#  Date Last Modified: 4/18/2022

import sys

class Node (object):
    def __init__ (self, data):
      self.data = data
      self.lChild = None
      self.rChild = None


class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
      self.root = None
      for char in encrypt_str:
          self.insert(char)

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
      new = Node(ch)
      
      if self.root != None:
          index   = self.root
          first = self.root
          while index  != None:
              first = index 
              if ch > index .data:
                index  = index .rChild
              else:
                index  = index .lChild
          if ch > first.data:
              first.rChild = new
          else:
              first.lChild = new
              
      else:
          self.root = new

      

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def in_tree (self, key):
    index  = self.root
    
    while (index.data != key) and (index != None):
      if key > index .data:
        index  = index .rChild
      else:
        index  = index .lChild
    return index  
        
  def search (self, ch):
      index  =self.root
      empty = ''
      
      if ch == self.root.data:
            return '*'
      elif self.in_tree(ch) == None:
            return ''

      while (index.data != ch) and (index != None): 
          if ch > index.data:
              empty = empty + '>'
              index = index.rChild
          else:
              empty = empty + '<'
              index = index.lChild
      return empty


  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
      index = self.root
      if st == "*":
        return self.root.data
      
      length = len(st)
      for position in range(length):
        if index != None and position == '<':
          index = index.lChild
        elif index != None and position == '>':
          index = index.rChild
        else:
          return ''
      return index.data
              
       

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
      
      if st == '':
        return ''
      
      st = st.lower()
      empty = ''
      length = len(st)
      for position in st:
          if position.isalpha():
            empty = empty + position
          elif position == " ":
            empty = empty + position

      encrytpted = ""

      for position in empty:
        index_encrypted = self.search(position)
        encrytpted = encrytpted + index_encrypted + "!"

      final = encrytpted[0:-1]
      return final

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    empty =  ""
    params = ['>','<','!','*']
    for position in st:
      if position in params:
          empty = empty + position

    lists = empty.split('!')

    decrypted = ""

    for position in lists:
            decrypted = decrypted + self.traverse(position)

    return decrypted

def main():
  # read encrypt string
  line = sys.stdin.readline()
  encrypt_str = line.strip()

  # create a Tree object
  the_tree = Tree (encrypt_str)

  # read string to be encrypted
  line = sys.stdin.readline()
  str_to_encode = line.strip() 

  # print the encryption
  print (the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
  line = sys.stdin.readline()
  str_to_decode = line.strip()
  
  # print the decryption
  print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
  main()
