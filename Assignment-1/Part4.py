#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:40:55 2022

@author: Anıl Alper
"""

class Node:
    def __init__(self, val:int):
        self.val = val
        self.nextElement = None
        
    
class LinkedList:
    def __init__(self):
        self.firstNode = None
        self.size = 0 
    
    def push(self, node:Node):
        if self.size == 0:
            self.firstNode = node
        else:
            curNode = self.firstNode
            while (curNode.nextElement != None):
                curNode = curNode.nextElement
            curNode.nextElement = node
            
        self.size += 1
    
    def pop(self) -> Node:
        if (self.size == 1):
            self.firstNode = None
        else:
            prevNode = self.firstNode
            curNode = self.firstNode.nextElement
            
            while (curNode.nextElement != None):
                prevNode = prevNode.nextElement
                curNode = curNode.nextElement
            
            prevNode.nextElement = None
        
        self.size -= 1
            
        return curNode
    
    def insert(self, index:int, node:Node):
        if index == 0:
            node.nextElement = self.firstNode
            self.firstNode = node
            self.size += 1
        elif index == self.size:
            self.push(node)
        else:
            if 0 < index < self.size:
                prevNode = self.firstNode
                nextNode = prevNode.nextElement
                
                for i in range(index-1):
                    prevNode = prevNode.nextElement
                    nextNode = nextNode.nextElement
                
                prevNode.nextElement = node
                node.nextElement = nextNode
                self.size += 1
    
    def remove(self, index:int):
        if self.size > 0:
            if (index == 0):
                self.firstNode = self.firstNode.nextElement
                self.size -= 1
            else:
                prevNode = self.firstNode
                curNode = prevNode.nextElement
                
                if 0 < index < self.size:
                    for i in range(index-1):
                        prevNode = prevNode.nextElement
                        curNode = curNode.nextElement
                    
                    prevNode.nextElement = curNode.nextElement
                    self.size -= 1
    
    def elementAt(self, index:int)->Node:
       if 0 <= index < self.size:
           curNode = self.firstNode
           
           for i in range(index):
               curNode = curNode.nextElement
             
           return curNode
       else:
           return None
       
        
    def getSize(self) ->int:
        return self.size
    
    def printList(self):
        list_str = ""
        curNode = self.firstNode
        for i in range(self.size):
            if (i != self.size-1):
                list_str += str(curNode.val) + " -> "
            else:
                list_str += str(curNode.val)
            
            curNode = curNode.nextElement
        print(list_str)


#Tests
#lst = LinkedList()
'''
#testPushBackAddsOneNode
for i in range(10):
    lst.push(Node(i))
lst.printList()

#testPopBackRemovesCorrectNode
lst.pop()
lst.pop()
lst.printList()

#testEraseRemovesCorrectNode
lst.remove(2)
lst.remove(0)
lst.remove(lst.getSize()-1) 
lst.printList()

#testEraseDoesNothingIfNoNode
lst.remove(100)
lst.remove(7)
lst.printList()

#testElementAtReturnNode
print(lst.elementAt(2))
print(lst.elementAt(0))

#testElementAtReturnsNoNodeIfIndexDoesNotExist
print(lst.elementAt(100))

#testSizeReturnsCorrectSize
print(lst.getSize())

for i in range(3):
    lst.pop()

lst.printList()
print(lst.getSize())
'''


            
        
            
