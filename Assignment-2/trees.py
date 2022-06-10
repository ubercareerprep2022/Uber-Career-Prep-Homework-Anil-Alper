#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 19:05:32 2022

@author: Anıl Alper
"""
from csv import reader
from datetime import datetime


class TreeNode:
    def __init__(self, val:int):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root:TreeNode):
        self.root = root
        
#Exercise 1: Printing a Tree
def printTree(tree):
    printNodes(tree.root)

def printNodes(cur_node):
    print(cur_node.val)
    
    if cur_node.left != None:
        printNodes(cur_node.left)
    
    if cur_node.right != None:
        printNodes(cur_node.right)

#Test Case:
node1 = TreeNode(1)
node1.left = TreeNode(7)
node1.right = TreeNode(17)
node1.right.right = TreeNode(3)
node1.right.left = TreeNode(6)

tree1 = Tree(node1)
#printTree(tree1)

#Exercise 2 and 3: Printing a Tree Level by Level and Printing the Number of Levels
class Employee:
        def __init__(self, name:str, title:str, directReports:list):
            self.name = name
            self.title = title
            self.directReports = directReports
            
class OrganizationStructure:        
    def __init__(self, employee:Employee):
        self.employee = employee

    def printLevelByLevel(self):
        queue = [self.employee]
        prev_level = 0
        level_queue = [0]
        while (len(queue) != 0):
            cur_head = queue.pop(0)
            cur_level = level_queue.pop(0)
            if cur_level >  prev_level:
                 print() 
            print("Name: " + str(cur_head.name) + ", Title: " + str(cur_head.title))
            for e in cur_head.directReports:
                queue.append(e)
                level_queue.append(cur_level+1)
            prev_level = cur_level
    
    def printNumLevels(self):
        cur_level = 1
        queue = [self.employee]
        level_queue = [1]
        
        while (len(queue) != 0):
            cur_level = level_queue.pop(0)
            cur_head = queue.pop(0)
            for e in cur_head.directReports:
                queue.append(e)
                level_queue.append(cur_level+1)
        
        print(cur_level)
           

intern = Employee("K", "Sales Intern", [])


engineerF = Employee("F", "Engineer", [])
engineerG = Employee("G", "Engineer", [])
engineerH = Employee("H", "Engineer", [])
representative = Employee("J", "Sales Representative", [intern])

director = Employee("I", "Director", [representative])
managerD = Employee("D", "Manager", [engineerF, engineerG, engineerH])
managerE = Employee("E", "Manager", [])

cfo = Employee("B", "CFO", [director])
cto = Employee("C", "CTO", [managerD, managerE])

ceo = Employee("A", "CEO", [cfo, cto])

org_structure = OrganizationStructure(ceo)

org_structure.printLevelByLevel()
org_structure.printNumLevels()


#Exercise 4: Implement a Binary Search Tree
class BinarySearchTree:
    def __init__(self, root):
        self.root = root
        
    def insert(self, val):
        cur_node = self.root
        self.insert_helper(val, cur_node)
    
    def insert_helper(self, val, cur_node):
        if cur_node.val >= val:
            if cur_node.left != None:
                self.insert_helper(val, cur_node.left)
            else:
                cur_node.left = TreeNode(val)
        else:
            if cur_node.right != None:
                self.insert_helper(val, cur_node.right)
            else:
                cur_node.right = TreeNode(val)
        
    def find(self, val):
        cur_node = self.root
        return self.find_helper(val, cur_node)
    
    def find_helper(self, val, cur_node):
        if cur_node.val > val:
            if cur_node.left != None:
                return self.find_helper(val, cur_node.left)
            else:
                return False
        elif cur_node.val < val:
            if cur_node.right != None:
                return self.find_helper(val, cur_node.right)
            else:
                return False
        else:
            return True
        
#Test Cases:
first_node = TreeNode(1)
tree = BinarySearchTree(first_node)
tree.insert(5)
print(tree.find(1))
print(tree.find(2))
print(tree.find(0))
tree.insert(0)
print(tree.find(0))
tree.insert(8)

print()
#Exercise 5: Implement a phone book
class ListPhoneBook:
    def __init__(self):
        self.nums = 0
        self.lst = list()
    
    def size(self):
        return self.nums
    
    def insert(self, name, number):
        self.lst.append([name, number])
        self.nums += 1
    
    def find(self, name):
        for i in range(self.size()):
            if self.lst[i][0] == name:
                return self.lst[i][1]
        return -1

class BinarySearchTreePhoneBook:
    def __init__(self):
        self.nums = 0
        self.tree = BinarySearchTree(TreeNode(["a", 0]))
        
    def size(self):
        return self.nums
    
    def insert(self, name, number):
        self.tree.insert([name, number])
        self.nums += 1
    
    def find(self, name):
        cur_node = self.tree.root
        return self.find_helper(name, cur_node)
    
    def find_helper(self, val, cur_node):
        if cur_node.val[0] > val:
            if cur_node.left != None:
                return self.find_helper(val, cur_node.left)
            else:
                return -1
        elif cur_node.val[0] < val:
            if cur_node.right != None:
                return self.find_helper(val, cur_node.right)
            else:
                return -1
        else:
            return cur_node.val[1]
        
#Exercise 6: Unsorted Lists v.s. Binary Search Trees

def exercise_6(lst):
    with open('data.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        lst_start = datetime.now()
        for row in csv_reader:
            lst.insert(row[0], row[1])
        lst_end = datetime.now()
    print("Insert took " + str((lst_end - lst_start).microseconds / 1000) + " milliseconds.")
        
    if lst.size() == 1000000:
        print("The size of the phone book is " + str(lst.size()) + ".")
    else:
        raise Exception("The size of this phone book is not equal to 1000000.")
    
    find_calls = 0
    with open("search.txt") as file:
        lst_start = datetime.now()
        for name in file:
            if lst.find(name.rstrip()) == -1:
                raise Exception("Name not found.")
            else:
                find_calls += 1
        lst_end = datetime.now()
        time_find = str((lst_end - lst_start).microseconds / 1000) 
    
    print("find() was called " + str(find_calls) + " times.")
    print("Search took " + str(time_find) + " milliseconds.")
    print()

#First Version
exercise_6(ListPhoneBook())
#Second Version
exercise_6(BinarySearchTreePhoneBook())

'''
1. What is the output of your program when you use a ListPhoneBook?

Insert took 959.923 milliseconds.
The size of the phone book is 1000000.
find() was called 1000 times.
Search took 922.418 milliseconds.

2. What is the output of your program when you use a BinarySearchTreePhoneBook?

Insert took 995.65 milliseconds.
The size of the phone book is 1000000.
find() was called 1000 times.
Search took 23.509 milliseconds.

3. Why is there a difference in the running times for the two implementations?

Insertion takes more time when using Binary Search Tree because it O(log(N)) instead of 
O(1) as in the List implementation. 
Search takes more time when using the List implementation because it is O(N) instead of
O(log(N)) as in Binary Search Tree
'''
