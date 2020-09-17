"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) < 1:
#             return None
#         else:
#             return self.storage.pop()

class Stack:
    class Node:
        def __init__(self, value, next_node = None):
            self.value = value
            self.next_node = next_node
    def __init__(self):
        self.size = 0
        self.head = None
        # self.storage = ?

    def __len__(self):
        return self.size

    def push(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            result = self.head.value
            self.head = self.head.next_node
            self.size -= 1
            return result


