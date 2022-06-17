#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 21:22:37 2022

@author: Anıl Alper
"""

#Exercise 1: Implement a graph using adjacency list 
#Exercise 2: DFS Traversal
#Exercise 3: BFS Traversal
#Exercise 4: Minimum Number of Edges Between Two Nodes of a Graph

class GraphNode:
    def __init__(self, data:int):
        self.data = data
    
class GraphWithAdjacencyList:
    def __init__(self):
        self.adjNodes = dict()
    
    def addNode(self, key:int):
        self.adjNodes[key] = list()
    
    def removeNode(self, key:int):
        del self.adjNodes[key]
    
    def addEdge(self, node1:int, node2:int):
        if self.adjNodes.get(node1) == None:
            self.addNode(node1)
            
        if self.adjNodes.get(node2) == None:
            self.addNode(node2)
        
        self.adjNodes[node1].append(node2)
        self.adjNodes[node2].append(node1)
    
    def removeEdge(self, node1:int, node2:int):
        self.adjNodes[node1].remove(node2)
        self.adjNodes[node2].remove(node1)
    
    def getAdjNodes(self, key:int)->list:
        return self.adjNodes[key]
    
    def DFS(self, key:int):
        self.DFSHelper(key, dict())
        
    def DFSHelper(self, key:int, explored:dict):
        print(key)
        explored[key] = "e"
        for n in self.adjNodes[key]:
            if explored.get(n) == None:
                self.DFSHelper(n, explored)
    
    def BFS(self, key:int):
        queue = list()
        queue.append(key)
        
        explored = dict()
        explored[key] = "e"   
        while (len(queue) != 0):
            cur_node = queue.pop(0)
            print(cur_node)
            for n in self.adjNodes[cur_node]:
                if explored.get(n) == None:
                    queue.append(n)
                    explored[n] = "e"
    
    def minNumberOfEdges(self, node1:int, node2:int):
        queue = list()
        queue.append((node1,0))
        
        explored = dict()
        explored[node1] = "e"   
        while (len(queue) != 0):
            cur_node = queue.pop(0)
            node = cur_node[0]
            cur_distance = cur_node[1]

            for n in self.adjNodes[node]:
                if explored.get(n) == None:
                    if n == node2:
                        return cur_distance+1
                    queue.append((n, cur_distance+1))
                    explored[n] = "e"
            
            

#Test Cases
#BFS and DFS
g = GraphWithAdjacencyList()
g.addEdge(0,2)
g.addEdge(0,1)
g.addEdge(2, 3)
#g.DFS(2)
#g.BFS(2)

#Minimum Number of Edges
g = GraphWithAdjacencyList()
g.addEdge(5,4)
g.addEdge(5,2)
g.addEdge(3,4)
g.addEdge(4,0)
g.addEdge(4,6)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)

print(g.minNumberOfEdges(1, 5))
print(g.minNumberOfEdges(6, 1))



