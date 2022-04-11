#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:21:22 2022

@author: Anıl Alper
"""

from Part4 import LinkedList, Node

def reverseLinkedListIter(lst: LinkedList) -> LinkedList:
    prev = None
    cur = lst.firstNode
    while (cur != None):
        nextprev = cur
        nextcur = cur.nextElement
        
        cur.nextElement = prev
        
        prev = nextprev
        cur = nextcur
        
        if  cur == None:
            lst.firstNode = prev
    return lst
            
def reverseLinkedListStack(lst: LinkedList) -> LinkedList:
    stack = list()
    cur = lst.firstNode
    
    while (cur != None):
        stack.append(Node(cur.val))
        cur = cur.nextElement
        
    new_lst = LinkedList()
    while (len(stack) > 0):
        node = stack.pop(len(stack)-1)
        new_lst.push(node)
        
    return new_lst

def reverseLinkedListRecursive(lst: LinkedList) -> LinkedList:
    new_lst = LinkedList()
    if lst.getSize() == 0:
        return new_lst
    if lst.getSize() == 1:
        new_lst.push(lst.firstNode)
        return new_lst
    curNode = Node(lst.firstNode.val)
    lst.remove(0)
    new_lst = reverseLinkedListRecursive(lst)
    new_lst.push(curNode)
    return new_lst
        
'''
# test 1 iteration
lst1 = LinkedList()
lst1.push(Node(1))
lst1.push(Node(2))
lst1.push(Node(3))
lst1.push(Node(4))

lst1.printList()
    
reverseLinkedListIter(lst1)

lst1.printList()

#test 2 iteration
lst2 = LinkedList()
lst2.push(Node(1))

lst2.printList()

reverseLinkedListIter(lst2)

lst2.printList()

#test 3 iteration
lst3 = LinkedList()
lst3.printList()

reverseLinkedListIter(lst3)

lst3.printList()
'''
'''
# test 1 stack
lst1 = LinkedList()
lst1.push(Node(1))
lst1.push(Node(2))
lst1.push(Node(3))
lst1.push(Node(4))

lst1.printList()
    
new_lst1 = reverseLinkedListStack(lst1)

new_lst1.printList()

#test 2 stack
lst2 = LinkedList()
lst2.push(Node(1))

lst2.printList()

new_lst2 = reverseLinkedListStack(lst2)

new_lst2.printList()

#test 3 stack
lst3 = LinkedList()
lst3.printList()

new_lst3 = reverseLinkedListStack(lst3)

new_lst3.printList()
'''

'''
# test 1 recursive
lst1 = LinkedList()
lst1.push(Node(1))
lst1.push(Node(2))
lst1.push(Node(3))
lst1.push(Node(4))

lst1.printList()
    
new_lst1 = reverseLinkedListRecursive(lst1)

new_lst1.printList()

#test 2 recursive
lst2 = LinkedList()
lst2.push(Node(1))

lst2.printList()

new_lst2 = reverseLinkedListRecursive(lst2)

new_lst2.printList()

#test 3 recursive
lst3 = LinkedList()
lst3.printList()

new_lst3 = reverseLinkedListRecursive(lst3)

new_lst3.printList()
'''