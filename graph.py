import networkx as nx
from networkx.drawing.nx_agraph import to_agraph #Requires pygraphviz
from addedFunctions import *

def main():
    DrawGraph = True

    edgeList = [
        [1,1],
        [1,2],
        [2,3,4],
        [3,3,5],
        [4,4,5],
        [5,1, 5]
    ]
    # edgeList = [
    #     [1,2,3], #1-->2,1-->3
    #     [2,2,4,6], # 2-->2, 2-->4, 2-->6
    #     [3,5],
    #     [6,5]
    # ]

    G = diGraphWithEdges(edgeList)

    if(DrawGraph):
        drawGraph(G, 'zGraph.png')


if __name__== "__main__":
  main()
