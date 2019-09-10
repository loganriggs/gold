from frequencyGraph import FrequencyGraph

edgeList = [
    [0, 0, 1],  # Note: must zero-index graph
    [1, 1, 0],
]
G = FrequencyGraph(edgeList)
print(G.frequencies())
G.drawFrequencyGraph("graph.png")