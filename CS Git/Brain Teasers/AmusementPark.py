
class Link (object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
class LinkedList (object):
    def __init__(self):
        self.first = None
    def insertFirst(self, data):
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink
    def insertLast(self, data):
        newLink = Link(data)
        current = self.first
        if (current == None):
            self.first = newLink
            return
        while (current.next != None):
            current = current.next
        current.next = newLink
    def findLink(self, data):
        current = self.first
        if (current == None):
            return None
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next
        return current
    def deleteLink(self, data):
        current = self.first
        previous = self.first
        if (current == None):
            return None
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next
        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next
        return current


# **DO NOT MODIFY ANYTHING ABOVE THIS LINE.**
# Return a linked list with the heights of the children after arranging them
#   based on whether or not they meet the roller coaster height requirement, h.
# You must use the Link and LinkedList classes to complete this question.
# You are **NOT ALLOWED** to use built-in data structures such as lists, sets, dicts,
#   or tuples to store the heights.
def arrangeChildren(heights: LinkedList, h: int) -> LinkedList:
    children_above_h = LinkedList()

    if heights.first != None:
        children_above_h.insertFirst(heights.first.data)
        head = heights.first
        while head.next != None:
            if head.next.data >= h:
                children_above_h.insertFirst(head.next.data)
            else:
                children_above_h.insertLast(head.next.data)
            head = head.next
        return children_above_h
    else:
        return children_above_h

    
            
    
            
        
        
    
    
    
     
