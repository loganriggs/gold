#These are functions written that are incomplete but may prove useful in the future.


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

def matrixFrequency(freqVect):
    sizePaths = len(freqVect)
    sizeStates = len(freqVect[0])
    matrixF = np.empty([sizePaths ,sizeStates])
    for fInd in range(sizePaths):
        matrixF[fInd] = freqVect[fInd]

    zeroSolution = np.zeros([sizePaths-1,sizeStates])
    solutionDegree = 0.001
    zeroSolution += solutionDegree

    for fInd in range(sizePaths):
        matrixTemp = matrixF[0 + 1:, :] - matrixF[0, :]
        sol = np.linalg.solve(matrixTemp, zeroSolution)
        print(sol)
    matrixF[:,0] *=.526
    matrixF[:,1] *=.474
    print(matrixF)
    return
