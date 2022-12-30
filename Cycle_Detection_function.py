from collections import defaultdict
import random
from turtle import color
from venv import create
import networkx as nx
import matplotlib.pyplot as plt

class CreateGraph(): #this class will create graph
	def addEdge(self,u,v): #for adding edge between two vertices
		self.graph[u].append(v)

	def checkCyclic(self, v, visited, stack): #will check for cycle recursive

		visited[v] = True
		stack[v] = True

		
		for link_with in self.graph[v]:
			if visited[link_with] == True:
				if stack[link_with] == True:
					print('Loop Found', v,link_with) #if loop found this will be printed
			if visited[link_with] == False:
				if self.checkCyclic(link_with, visited, stack) == True:
					return True
			elif stack[link_with] == True:
				return True

		stack[v] = False
		return False
	
	def __init__(self,vertices): #constructor of graph class take paramter as a number of vertices
		self.graph = defaultdict(list)
		self.V = vertices
    
	def isCyclic(self): #will call detect cycle above functin
		visited = [False] * (self.V + 1)
		recStack = [False] * (self.V + 1)
		for node in range(self.V):
			if visited[node] == False:
				if self.checkCyclic(node,visited,recStack) == True:
					return True
		return False

f = open("example_Graph.txt","r") #to read graph data from txt file
firstLine = True
concat = ''
concat2 = ''
flag = False
for line in f: #reading data line by line
	if(firstLine): #first line is vertices number
		verticesNo = line
		g = CreateGraph(int(verticesNo)) #creating graph vertices
		firstLine = False
	else: #reading edges
		for x in line:
			if(x!=','):
				concat = concat + x
			else:
				concat2 = concat
				concat = ''
		g.addEdge(int(concat2), int(concat)) #convert string to int then adding edge
	concat = ''
	concat2 = ''
if g.isCyclic() != 1:  #checking for cycle by  calling method of graph class
	print("None")