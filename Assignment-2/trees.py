#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 19:05:32 2022

@author: Anıl Alper
"""
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


#Exercise 5: Implement a phone book
    
    
