from addedFunctions import *

def main():
    edgeList = [
        [0,0], #Note: must zero-index graph
        [0,1],
        [1,2,3],
        [2,2,4],
        [3,3,4],
        [4,0, 4]
    ]
    # edgeList = [
    #     [0,1,2], #0-->1,0-->2
    #     [1,1,3,5], # 1-->1, 1-->3, 1-->5
    #     [2,4],
    #     [5,4]
    # ]

    gamma = .90
    G = diGraphWithEdges(edgeList)
    f = frequencyVectors(G,gamma)
    drawGraph(G, "graphWithoutFrequencies.png")
    drawFrequency(G, "graphWithF.png", f)


if __name__== "__main__":
  main()
