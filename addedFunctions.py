import networkx as nx
from networkx.drawing.nx_agraph import to_agraph #Requires pygraphviz
import numpy as np
import math
#-----------Globals---------------
freqVector = []

#Shortest Path:
#nx.shortest_path(G)

def diGraphWithEdges(eList):
    tempG = nx.DiGraph()
    for subList in eList:
        for index in range(1, len(subList)):
            tempG.add_edge(subList[0], subList[index])
    return tempG

def stateVisitationFrequencyVector(graph):
    return

def cyclesOf(graph):
    return nx.simple_cycles(graph)


def drawGraph(graph, name):
    A = to_agraph(graph)
    A.layout('dot')
    A.draw(name)  # Look in file directory for this!

def drawFrequency(graph,name, frequency):
    for n in graph: #is this 0,1,2, or actual "ham" labels
        labelName = str(n)
        for f in frequency[n]:
            labelName += "\n"+str(f)
        graph.node[n]['label'] = labelName
    A = to_agraph(graph)
    A.layout('dot')
    A.draw(name)

# def dfs(G, source=None, depth_limit=None):
#     if source is None:
#         # edges for all components
#         nodes = G
#     else:
#         # edges for components with source
#         nodes = [source]
#     visited = set()
#     if depth_limit is None:
#         depth_limit = len(G)
#     for start in nodes:
#         if start in visited:
#             continue
#         visited.add(start)
#         stack = [(start, depth_limit, iter(G[start]))]
#         while stack:
#             parent, depth_now, children = stack[-1]
#             try:
#                 child = next(children)
#                 if child not in visited:
#                     yield parent, child
#                     visited.add(child)
#                     if depth_now > 1:
#                         stack.append((child, depth_now - 1, iter(G[child])))
#             except StopIteration:
#                 stack.pop()

def graphTests(gamma):
    edgeListOneLoop = [
        [0, 0]
    ]
    oneLoop = diGraphWithEdges(edgeListOneLoop)
    solutionOneLoop = [
        [
            np.array([
                1/(1-gamma)
            ])
        ]
    ]

    edgeListOneTwoLoop = [
        [0, 1],
        [1, 1]
    ]
    oneTwoLoop = diGraphWithEdges(edgeListOneTwoLoop)
    solutionOneTwoLoop = [
        [
            np.array([
                1,
                gamma/(1-gamma)
            ])
        ],
        [
            np.array([
                0,
                1 / (1 - gamma)
            ])
        ]
    ]


    edgeListOneTwoOne = [
        [0, 1],
        [1, 0]
    ]
    oneTwoOne = diGraphWithEdges(edgeListOneTwoOne)
    solutionOneTwoOne = [
        [
            np.array([
                1/ (1 - gamma**2),
                gamma / (1 - gamma**2)
            ])
        ],
        [
            np.array([
                gamma / (1 - gamma**2),
                1 / (1 - gamma**2)
            ])
        ]
    ]



    edgeListOneLoopTwoLoopOne = [
        [0, 0, 1],
        [1, 1, 0]
    ]
    oneLoopTwoLoopOne = diGraphWithEdges(edgeListOneLoopTwoLoopOne)
    solutionOneLoopTwoLoopOne = [
        [
            np.array([
                1 / (1 - gamma),
                0
            ]),
            np.array([
                1,
                gamma / (1 - gamma)
            ]),
            np.array([
                1 / (1 - gamma ** 2),
                gamma / (1 - gamma ** 2)
            ])
        ],
        [
            np.array([
                0,
                1 / (1 - gamma)
            ]),
            np.array([
                gamma / (1 - gamma),
                1
            ]),
            np.array([
                gamma / (1 - gamma ** 2),
                1 / (1 - gamma ** 2)
            ])
        ]
    ]


    edgeListOneTwoThreeLoopAndOneThree = [
        [0, 1, 2],
        [1, 2],
        [2,2]
    ]
    oneTwoThreeLoopAndOneThree = diGraphWithEdges(edgeListOneTwoThreeLoopAndOneThree)
    solutionOneTwoThreeLoopAndOneThree = [
        [
            np.array([
                1,
                gamma,
                gamma**2 / (1 - gamma)
            ]),
            np.array([
                1,
                0,
                gamma / (1 - gamma)
            ])
        ],
        [
            np.array([
                0,
                1,
                gamma / (1 - gamma)
            ])
        ],
        [
            np.array([
                0,
                0,
                1 / (1 - gamma)
            ])
        ]
    ]

    edgeListOneTwoLoopAndThreeTwo = [
        [0, 1],
        [1, 1],
        [2, 1]
    ]
    oneTwoLoopAndThreeTwo = diGraphWithEdges(edgeListOneTwoLoopAndThreeTwo)
    solutionOneTwoLoopAndThreeTwo = [
        [
            np.array([
                1,
                gamma/(1 - gamma),
                0
            ])
        ],
        [
            np.array([
                0,
                1 / (1 - gamma),
                0
            ])
        ],
        [
            np.array([
                0,
                gamma / (1 - gamma),
                1
            ])
        ]
    ]


    graphList = [oneLoop, oneTwoLoop, oneTwoOne, oneLoopTwoLoopOne, oneTwoThreeLoopAndOneThree, oneTwoLoopAndThreeTwo]
    graphNames = ["oneLoop", "oneTwoLoop", "oneTwoOne", "oneLoopTwoLoopOne", "oneTwoThreeLoopAndOneThree", "oneTwoLoopAndThreeTwo"]
    solutionList = [solutionOneLoop, solutionOneTwoLoop, solutionOneTwoOne, solutionOneLoopTwoLoopOne,
                    solutionOneTwoThreeLoopAndOneThree, solutionOneTwoLoopAndThreeTwo]
    freq = []
    for graph in graphList:
        freq.append(frequencyVectors(graph, gamma))
    for ind in range(len(graphList)):
        # assert frequencySanitySumCheck(f, gamma), "Frequency Vector did not sum to 1/(1-gamma)!"
        # assert f == solutionList[ind], "Frequency Vector did not match test case {0}!".format(graphNames[ind])
        try:
            for f1,f2 in zip(freq[ind],solutionList[ind]):
                for ff1, ff2 in zip(f1,f2):
                    for val1, val2 in zip(ff1,ff2):
                        if not math.isclose(val1,val2, rel_tol=.01):
                            assert 0
        except:
            print(freq[ind])
            print(solutionList[ind])
            assert 0, "Frequency Vector did not match test case {0}!".format(graphNames[ind])
        drawFrequency(graphList[ind], graphNames[ind]+".png", freq[ind])

def frequencySanitySumCheck(fVector, gamma):
    sumCheck = 1/(1-gamma)
    return sumCheck == np.sum(fVector)

def frequencyVectors(graph, gamma):
    #Depth first search through graph

    #Global values
    global freqVector
    sSize = graph.number_of_nodes()
    freqVector =  [[] for i in range(sSize)]
    gammaAll = [gamma**i for i in range(sSize)]
    cycleDenominatorAll = [1/(1-gamma**i) for i in range(1, sSize+1)]
    e = np.eye(sSize)
    nodesVisited = []


    for currentNode in graph:
        # if currentNode in nodesVisited:
        #     continue
        # Local Values that are appended, popped, incremented. They change on a resursive basis.
        localNodesVisited = [currentNode]
        localFreqVector = np.zeros(sSize)
        localFreqVector[currentNode] = 1
        depth = 0
        initialNode = currentNode
        nodesVisited.append(currentNode)
        frequencyVectorsRecursionHelper(depth, localNodesVisited, localFreqVector, currentNode, initialNode, nodesVisited,  gammaAll, cycleDenominatorAll, e, graph)

    return freqVector

def frequencyVectorsRecursionHelper(depth, localNodesVisited, localFreqVector,  currentNode,  initialNode, nodesVisited, gammaAll, cycleDenominatorAll, e, graph):
    # depth        - depth of current path
    # localNodesVisited - nodes visited on current path. Used to determine cycles
    # localFreqVector - freq vector of current path starting from the original "currentNode"
    # initialNode    - Initial node when this function was first called. Used to calculate global frequency vectors
    # currentNode    - # of node of current path
    # nodesVisited - nodes visited at all. Used to determine if you've already been to a node to reuse the f-vector (dynamic programming)
    # gammaAll - Pre-computed gamma discounts
    # cycleDenominatorAll - Pre-computed gamma denominators for cycles
    # e - basis Vector
    # graph - the graph we're find the frequency vector for
    global freqVector
    # freqVector - global frequency vector that is updated

    for nhb in graph[currentNode]:
        if(nhb in localNodesVisited): #Found a cycle
            k = depth - localNodesVisited.index(nhb)
            scalar = cycleDenominatorAll[k]
            indexRangeOfLoop = localNodesVisited[depth-k: depth+1]
            # print(k)
            # print(scalar)
            # print(indexRangeOfLoop)
            # print(localFreqVector)
            # localFreqVector[indexRangeOfLoop] *= scalar
            #Logan, maybe TODO scacel afterwards? liek line 298?

            #Save global Freq for initial node
            freqVector[initialNode].append(np.copy(localFreqVector))
            freqVector[initialNode][-1][indexRangeOfLoop] *= scalar
            #Use that to determine all other nodes in path
            # for visInd in range(1, len(localNodesVisited)):
            #     presentNode = localNodesVisited[visInd]
            #     pastNode = localNodesVisited[visInd - 1]
            #     #f1 = (f0-e)/gamma
            #     freqVector[presentNode].append((freqVector[pastNode][-1] - e[pastNode])/gammaAll[1])
            continue

        # elif(nhb in nodesVisited): #Found previously visited node
        #TODO this will help wtih dynamic saving, but only in certain cases.
        #TODO haven't figured out how to do that yet.
        #     # for each frequency in found node, append it to our inital
        #     freqCount = 0
        #     for frequency in freqVector[nhb]:
        #         freqVector[initialNode].append(
        #             np.copy(localFreqVector + gammaAll[depth+1]*np.copy(frequency))
        #         )
        #         freqCount +=1
        #     # Use that to determine all other nodes in path
        #     for visInd in range(1, len(localNodesVisited)):
        #         presentNode = localNodesVisited[visInd]
        #         pastNode = localNodesVisited[visInd - 1]
        #         # f1 = (f0-e)/gamma
        #         for newFrequencyIndex in range(freqCount):
        #             freqVector[presentNode].append((freqVector[pastNode][-1-newFrequencyIndex] - e[pastNode]) / gammaAll[1])
        #     #Does this even work? so complicated
        #     continue

        else: #Found new node, continue recursively
            depth += 1
            prevNode = currentNode
            currentNode = nhb

            localNodesVisited.append(currentNode)  # Used to determine cycles, popped up recursively
            localFreqVector[currentNode]  = gammaAll[depth]
            # nodesVisited.append(currentNode) #Not popped later

            frequencyVectorsRecursionHelper(depth, localNodesVisited, localFreqVector,  currentNode, initialNode,
                                            nodesVisited, gammaAll, cycleDenominatorAll, e, graph)
            localFreqVector[currentNode] = 0 #Like a pop
            currentNode = prevNode
            localNodesVisited.pop() #TODO test if I need to this = pop(this)
            depth -= 1
    return

def findAllPaths(graph):
    allPaths = []
    for n in graph:
        allPaths.extend(findAllPathsRecursiveHelper(graph, [], [n]) )
    return allPaths

def findAllPathsRecursiveHelper(graph, allPaths, localPaths):
    currentNode = localPaths[-1]
    for nhb in graph[currentNode]:
        if(nhb in localPaths): #Found a cycle
            l = localPaths.index(nhb)
            allPaths.append(localPaths[:])
            allPaths[-1].append(l)
        else:
            localPaths.append(nhb)
            # allPaths.append(findAllPathsRecursiveHelper(graph, allPaths, localPaths))
            findAllPathsRecursiveHelper(graph, allPaths, localPaths)
            localPaths.pop()
    return allPaths

def cyclesPrefixesOfPaths(paths):
    cycles = []
    prefixes = []
    for path in paths:
        if(path[-1]==0):
            cycles.append(path)
        else:
            prefixes.append(path)
    return cycles, prefixes

def assignFrequencies(cycles, prefixes, stateSize, gamma):
    #TODO incomplete
    freqVector = [[] for i in range(stateSize)]
    gammaAll = [gamma ** i for i in range(stateSize)]
    cycleDenominatorAll = [1 / (1 - gamma ** i) for i in range(1, stateSize + 1)]
    e = np.eye(stateSize)

    for cycle in cycles:
        k = len(cycle)-1 #Size of cycle. -1 for appended value from path-finder
        initialNode = cycle[0]
        freqVector[initialNode].append(np.zeros(stateSize))
        for stateIndex in range(k):
            freqVector[initialNode][-1][cycle[stateIndex]] = gammaAll[stateIndex]
        scalar = cycleDenominatorAll[k-1] #zero indexing, so -1
        freqVector[initialNode][-1] *= scalar
    for prefix in prefixes:
        cycleStarts = prefixes[-1]
        for prefixIndex in range(1,cycleStarts+1):
            f0 = cycleStarts - prefixIndex
            f1 = f0+1
            for frequency in freqVector[f1]:
                return
    return freqVector

def main():
    edgeList = [
        [0, 0, 1],
        [1, 1, 0]
    ]
    G = diGraphWithEdges(edgeList)
    stateSize = G.number_of_nodes()
    gamma = 0.90
    # paths = findAllPaths(G)
    # cycles, prefixes = cyclesPrefixesOfPaths(paths)
    # f = assignFrequencies(cycles, prefixes, stateSize, gamma)
    # f = frequencyVectors(G, gamma)
    # print(f)
    # drawGraph(G, "bam.png")
    # drawFrequency(G, "bamF.png", f)
    graphTests(gamma)
    return

if __name__ == "__main__":
    main()