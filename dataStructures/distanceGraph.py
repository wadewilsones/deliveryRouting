
#This file define graph where edges represent distance and vertices represent addresses

import re

class distanceGraph:

    #constructor
    def __init__(self, verticeNumber):
        #create list of num_vertices verices with null data (for addresses)
        self.vertices = [None] * verticeNumber
        #create list of num_vertices verices with null data (for distance)
        self.edges = [[float('inf')] * verticeNumber for _ in range(verticeNumber)]

    #update vertex
    def updateVertex(self, index, address):
        self.vertices[index] = address


    def getIndexOfVertex(self, vericeAddress):
        for index, vertice in  enumerate(self.vertices):
            if(''.join(vertice) == vericeAddress):
                return(index)

    #update edge
    def updateEdge(self, vertixIndex1, vertixIndex2, distance):
        self.edges[vertixIndex1][vertixIndex2] = distance
        self.edges[vertixIndex2][vertixIndex1] = distance


    #get distance between 2 vertices
    def get_distanceOfVertexes(self, vertixIndex1, vertixIndex2):

        return self.edges[vertixIndex1][vertixIndex2]
    
    #print
    def printVertex(self):
        for value in self.vertices:
            print (value)

    #print edge
    def printEdge(self):
        for value in self.edges:
            print (value)


    # convert vertice to String

    def convertToString(self):
        listofVertices = []
        for vertice in self.vertices:
            verticeStr = ""
            verticeStr = verticeStr.join(vertice)
            verticeStr.replace('(','').replace(')','')
            listofVertices.append(verticeStr)
            
        return listofVertices