from frequencyGraph import FrequencyGraph

edgeList = [
    [0, 0, 1],  # Note: must zero-index graph
    [1, 1, 0],
]
G = FrequencyGraph(edgeList)
G.drawFrequencyGraph("graph.png")