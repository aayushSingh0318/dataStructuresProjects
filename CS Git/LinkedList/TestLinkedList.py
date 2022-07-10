#  File: TestLinkedList.py

#  Description:

#  Student Name: Aayush Singh

#  Student UT EID: as92488

#  Partner Name: Danny Xie

#  Partner UT EID: dax56

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created:

#  Date Last Modified:

from typing import Counter


class Link (object):
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
    # create a linked list
    def __init__ (self):
        self.first = None

    # get number of links 
    def get_num_links (self):
        current_pos = self.first
        val = 0
        while current_pos:
            val = val + 1
            current_pos = current_pos.next
        return val
    # add an item at the beginning of the list
    def insert_first (self, data): 
        new = Link(data,self.first)
        self.first = new
    # add an item at the end of a list
    def insert_last (self, data): 
        if self.first == None:
            self.insert_first(data)
            return
        pos = self.first
        while pos.next!=None:
            pos = pos.next
        pos.next = Link(data,pos.next)
        return
    # add an item in an ordered list in ascending order
    def insert_in_order (self, data): 
    
        if data < self.first.data or self.first is None:
            self.insert_first(data)
            return
        pos = self.first
        while data > pos.next.data and pos.next:
            pos = pos.next
        pos.next = Link(data,pos.next)
        return
    # search in an unordered list, return None if not found
    def find_unordered (self, data): 
        if self.first:
            pass
        else:
            return None
        pos = self.first
        while not pos.next == None:
            if pos.data != data:
                pass
            else:
                return pos
            pos = pos.next
        return None

    # Search in an ordered list, return None if not found
    def find_ordered (self, data): 
        if self.first != None:
            pass
        else:
            return None
        current_pos = self.first
        while current_pos.data!= data:
            if current_pos.next:
                pass
            else:
                return None
            current_pos = current_pos.next
        return current_pos
    # Delete and return Link from an unordered list or None if not found
    def delete_link (self, data):
        if self.first:
            pass
        else:
            return None
        pos = self.first
        if pos.data !=data:
            pass
        else:
            self.first = pos.next
            return pos
        while pos.next!=None:
            if pos.next.data != data:
                pass
            else:
                eliminate = pos.next
                pos.next = eliminate.next
                return eliminate

            pos = pos.next
        return None
    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        stringrep = ''
        val_count = 0
        current_pos = self.first
        while current_pos:
            stringrep = stringrep + str(current_pos.data) + '  '
            current_pos = current_pos.next
            val_count = val_count + 1
            if val_count !=10:
                pass
            else:
                stringrep = stringrep + '\n'
                val_count = 0
        return stringrep
    # Copy the contents of a list and return new list
    def copy_list(self):
        new = LinkedList()
        current_pos = self.first

        while current_pos != None:
            new.insert_last(current_pos.data)
            current_pos = current_pos.next

        return new
    # Reverse the contents of a list and return new list
    def reverse_list (self): 
        new = LinkedList()
        current = self.first

        while current != None:
            new.insert_first(current.data)
            current = current.next

        return new
    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        new = LinkedList()
        current_pos = self.first

        while current_pos != None:
            new.insert_in_order(current_pos.data)

            if current_pos.next == None:
                break
            else:
                current_pos = current_pos.next

        return new
    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        new = LinkedList()
        current_pos = self.first

        while current_pos.next != None:
            if current_pos.data <= current_pos.next.data:
                current_pos = current_pos.next
            else:
                return False

        return True
    # Return True if a list is empty or False otherwise
    def is_empty (self): 
        if self.first != None:
            return False
        else:
            return True
    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        if self.is_empty():
            if other.is_empty():
                return None
            else:
                return other
        elif other.is_empty():
            return self
        current_pos = self.first
        while (current_pos.next != None):
            current_pos = current_pos.next

        current_pos.next = other.first

        merged = self.sort_list()
        return merged
    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        if self.is_empty() and other.is_empty():
            return True
        first = self.first
        second = other.first
        while not first.data != second.data:
            first = first.next
            second = second.next
            if first !=None and second !=None:
                pass
            elif first ==None and second ==None:
                return True
            elif first ==None or second ==None:
                return False
        return False

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        new = LinkedList()
        current_pos = self.first

        empty = []

        while current_pos != None:
            if not current_pos.data in empty:
                empty.append(current_pos.data)
                new.insert_last(current_pos.data)
            current_pos = current_pos.next

        return new
def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.

  # Test method insert_last()

  # Test method insert_in_order()

  # Test method get_num_links()

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 

  # Test method copy_list()

  # Test method reverse_list()

  # Test method sort_list()

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted

  # Test method is_empty()

  # Test method merge_list()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal

  # Test remove_duplicates()

    if __name__ == "__main__":
        main()