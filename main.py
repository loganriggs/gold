from frequencyGraph import FrequencyGraph

def main():
    edgeList = [
    #[state, connected state#1, connected state#2, ...]
        [0, 1],  # Note: must zero-index graph
        [1, 2],
        [2,3,2], #self-loops and multiple connections allowed
        [3,3]
    ]
    #Creates directed graph and determines frequencies
    G = FrequencyGraph(edgeList)
    #returns frequencies
    G.frequencies()
    #Creates .png of graph in current directory
    G.drawGraph("graphWithoutFrequencies.png")
    G.drawFrequencyGraph("graphWithFreq.png")
    return

if __name__== "__main__":
  main()
