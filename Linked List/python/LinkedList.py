class Node(object):
      def __init__(self, _data = None, _next = None):
        self.data = _data
        self.next= _next
        
      def get_data(self):
          return self.data

      def get_next(self):
        return self.next_node

      def set_next(self, new_next):
        self.next_node = new_next


class LinkedList (object):
    def __init__( self, head=None):
        self.head = head
    
    def push(self, key):
        node = Node(key)
        node.set_next(self.head)
        self.head = node
    
    def __str__(self):
        temp = self.head
        output = ""
        while temp:
            output = output + str(temp.get_data()) + "->"
            temp = temp.get_next()
        
        return output[:-2]






