#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 12:52:59 2022

@author: mollysandler
"""

# Stack class implemented with array
class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a Python 
List"""
    # capacity is max number of Nodes, init_items is optional List parameter for initialization
    # if the length of the init_items List exceeds capacity, raise IndexError
    def __init__(self, capacity, init_items=None):
            """Creates an empty stack with a capacity"""
            self.capacity = capacity        # capacity of stack
            self.items = [None]*capacity    # array for stack
            self.num_items = 0              # number of items in stack
           
            if init_items is not None:      # if init_items is not None, initialize stack
                if len(init_items) > capacity:
                    raise IndexError
                
                else:
                    self.num_items = len(init_items)
                    self.items[:self.num_items] = init_items
                    
    def __eq__(self, other):
            return ((type(other) == Stack)
                and self.capacity == other.capacity
                and self.items[:self.num_items] == other.items[:other.num_items])
        
    def __repr__(self):
        return ("Stack({!r}, {!r})".format(self.capacity, self.items[:self.num_items]))
    

    def is_empty(self): 
        if self.num_items == 0:
            return True
        else:
            return False
        '''Returns True if the stack is empty, and False otherwise
               MUST have O(1) performance'''
  
    def is_full(self): 
        if self.capacity == self.num_items:
            return True
        else:
            return False
            '''Returns True if the stack is full, and False otherwise
               MUST have O(1) performance'''
               
    def push(self, item):
        if not self.is_full():
            self.items[self.num_items] = item
            self.num_items += 1  
            return self.num_items
        else:
            raise IndexError
        
            '''If stack is not full, pushes item on stack. 
               If stack is full when push is attempted, raises IndexError
               MUST have O(1) performance'''
               
    def pop(self): 
        if not self.is_empty():
            temp = self.items[self.num_items -1]
            self.items[self.num_items -1] = None
            self.num_items -= 1
            return temp
            
        else: 
            raise IndexError
            '''If stack is not empty, pops item from stack and returns item.
               If stack is empty when pop is attempted, raises IndexError
               MUST have O(1) performance'''
   
    def peek(self):
        if not self.is_empty():
            return self.items[self.num_items -1]
        else:
            raise IndexError
            '''If stack is not empty, returns next item to be popped (but does not 
    remove the item)
               If stack is empty, raises IndexError
               MUST have O(1) performance'''
               
    def size(self):
        return self.num_items
        
        '''Returns the number of elements currently in the stack, not the capacity
               MUST have O(1) performance'''
               
#if __name__ == '__main__':
