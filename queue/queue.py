"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop(0)

class Queue:
    class Node:
        def __init__ (self, value, next_node = None):
            self.value = value
            self.next_node = next_node

        def set_next(self, new_next):
            self.next_node = new_next

        def get_value(self):
            return self.value

        def get_next(self): # forgotten def get_next caused Attribute Error
            return self.next_node
    
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = self.Node(value)
        self.size += 1
        if self.head is None and self.tail is None: # if statement was incorrect: 
            self.head = new_node                    # 'if self.head and self.tail is None:' results in AttributeError: 'NoneType' object has no attribute 'set_next'
            self.tail = new_node                    # results in AttributeError: 'NoneType' object has no attribute 'set_next'
       
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            result = self.head.get_value()
            self.head = self.head.get_next()
            self.size -= 1
            return result


       
