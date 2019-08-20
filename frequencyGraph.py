######################################################################
# Defines Class for the Frequency Graph
# Immediately creates directed graph from edgelist and determines
# frequencies for all states.
# Members:
# self.graph - networkx directed graph class. Has access to all
#              related functions by self.graph.function()
# self.frequency - frequency list of type [[ndarray()]]
#
# Functions:
# self.frequencies() - returns self.frequency
# self.drawGraph(name) - Draws directed graph saved as "name" in
#                        current directory
# self.drawFrequencyGraph(name) - Same as above, but with frequencies
#                                 included
#
# Other Functions used to create Frequency Graph class
# diGraphWithEdges(eList) - loops over networkx addNode() method to
#                           add edge list
# frequencyVectors(graph) - depth first search that determines
#                           frequency vectors
# frequencyVectorsRecursionHelper - Helps above
######################################################################

import networkx as nx
from networkx.drawing.nx_agraph import to_agraph #Requires pygraphviz
import numpy as np
import sympy

class FrequencyGraph:
    def __init__(self, edgeList):
        self.graph = diGraphWithEdges(edgeList)
        self.frequency = frequencyVectors(self.graph)
    def frequencies(self):
        return self.frequency
    def drawGraph(self, name):
        A = to_agraph(self.graph)
        A.layout('dot')
        A.draw(name)
    def drawFrequencyGraph(self, name):
        for n in self.graph:  # is this 0,1,2, or actual "ham" labels
            labelName = "State: "+ str(n) +"\n"
            for f in self.frequency[n]:
                labelName += "[ "
                fLength = len(f)
                for valueIndex in range(fLength):
                    valueString = str(f[valueIndex])
                    labelName += valueString
                    lengthOfValue = len(valueString)
                    labelName += " " * (14 - lengthOfValue)
                    if(valueIndex != fLength -1):
                        labelName += ", "
                labelName += "]\n"
            self.graph.node[n]['label'] = labelName
        A = to_agraph(self.graph)
        A.layout('dot')
        A.draw(name)


def diGraphWithEdges(eList):
    tempG = nx.DiGraph()
    for subList in eList:
        for index in range(1, len(subList)):
            tempG.add_edge(subList[0], subList[index])
    return tempG

def frequencyVectors(graph):
    gamma = sympy.Symbol("y")
    sSize = graph.number_of_nodes()
    freqVector =  [[] for i in range(sSize)]
    gammaAll = [gamma**i for i in range(sSize)]
    cycleDenominatorAll = [1/(1-gamma**i) for i in range(1, sSize+1)]

    for currentNode in graph:
        localNodesVisited = [currentNode]
        localFreqVector = np.array([sympy.Number(0) for i in range(sSize)])
        localFreqVector[currentNode] = sympy.Number(1)
        depth = 0
        frequencyVectorsRecursionHelper(depth, localNodesVisited, localFreqVector, currentNode,  gammaAll, cycleDenominatorAll,graph, freqVector)

    return freqVector

def frequencyVectorsRecursionHelper(depth, localNodesVisited, localFreqVector, initialNode, gammaAll, cycleDenominatorAll, graph, freqVector):
    currentNode = localNodesVisited[-1]
    for nhb in graph[currentNode]:
        if(nhb in localNodesVisited): #Found a cycle
            k = depth - localNodesVisited.index(nhb)
            indexRangeOfLoop = localNodesVisited[depth-k: depth+1]
            scalar = cycleDenominatorAll[k]
            freqVector[initialNode].append(np.copy(localFreqVector))
            freqVector[initialNode][-1][indexRangeOfLoop] *= scalar
        else: #Found new node, continue recursively
            depth += 1
            localNodesVisited.append(nhb)  # Used to determine cycles, popped up recursively
            localFreqVector[nhb]  = gammaAll[depth]

            frequencyVectorsRecursionHelper(depth, localNodesVisited, localFreqVector, initialNode,
                                            gammaAll, cycleDenominatorAll, graph, freqVector)

            localFreqVector[nhb] = 0 #Like a pop
            localNodesVisited.pop()
            depth -= 1
    return freqVector

def main(): #For testing in-file
    edgeList = [
        [0, 0, 1],
        [1, 1, 0]
    ]
    G = FrequencyGraph(edgeList)
    G.drawFrequencyGraph("graph.png")
    return

if __name__ == "__main__":
    main()