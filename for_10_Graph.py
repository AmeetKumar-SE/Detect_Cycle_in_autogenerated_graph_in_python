from collections import defaultdict
import random
from turtle import color
import networkx as nx
import matplotlib.pyplot as plt
import os
from os import listdir
import cv2


class CreateGraph(): #this class will create graph

	def addEdge(self,u,v): #for adding edge between two vertices
		self.graph[u].append(v)

	
	def checkCyclic(self, v, visited, stack): #will check for cycle recursive

		visited[v] = True
		stack[v] = True

		
		for link_with in self.graph[v]:
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
    
	
	
	def isCyclic(self): #will call detect cycle above function
		visited = [False] * (self.V + 1)
		recStack = [False] * (self.V + 1)
		for node in range(self.V):
			if visited[node] == False:
				if self.checkCyclic(node,visited,recStack) == True:
					return True
		return False



for i in range(10): #this will add N Graph
    
	g = CreateGraph(10) #this will add N  vertices in each graph
    
	gDraw = nx.Graph()
    
	pox = nx.spring_layout(gDraw) #show graph in  spring  layout
    
	for j in range(10):  #this will add N  edges
		
		r1 = random.randint(0,10)
		
		r2 = random.randint(0,10)
		
		g.addEdge(r1,r2)
        
		gDraw.add_edge(r1,r2)
    
	
	if g.isCyclic() == 1: #if there is cycle, this will draw graph in  black color
        
		nx.draw(gDraw, with_labels = True, node_color="black", arrows = True, font_color = 'yellow')
    
	else: #if no cycle, will draw graph in red color
        
		nx.draw(gDraw, with_labels = True, node_color="red", arrows = True, font_color='yellow')
    
	plt.savefig('graph'+str(i)+'.png') #will save each file as png format
    
	plt.clf() #clearing the  graph


nr = 5 #num of rows for grid
nc = 2 #num of columns for grid

photo_list = [] #will store collection of photos
Image_List = [] #store name of each graph

# get the path/directory
folder_dir = os.getcwd() #getting current directory path

for images in os.listdir(folder_dir): #reading every image from folder
	if (images.endswith(".png")): #selecting just png format pictures
		Image_List.append(folder_dir + '\\' + images) #adding  each image to list


fig = plt.figure(figsize=(15,15)) #for drawing images on grid 5*2


for i in range(nr*nc):
	images2 = cv2.imread(Image_List[i]) #reading each image
	plt.subplot(nr,nc,i+1) #defining subplot index
	plt.imshow(images2) #assiging  image to plot
	plt.axis('off') #not to show x-axis and y-axis

plt.show() #will show all images in single window