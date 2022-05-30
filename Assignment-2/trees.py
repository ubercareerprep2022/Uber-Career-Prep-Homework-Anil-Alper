#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 19:05:32 2022

@author: Anıl Alper
"""

class Tree:
    def __init__(self, root):
        self.root = root

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
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
printTree(tree1)

#Exercise 2: Printing a Tree Level by Level