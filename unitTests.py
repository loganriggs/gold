######################################################################
# Unit tests for frequencies. Can be added onto by
# 1. Defining edgeList
# 2. Creating Frequency Graph
# 3. Defining Solution
# 4. Adding to the graphList, graphNames, and SolutionList
#
# Unit tests are drawn upon verification and saved as their graphName
######################################################################
from frequencyGraph import FrequencyGraph
import numpy as np
import sympy
import math

def graphTests():
    gamma = sympy.Symbol("y")

    edgeListOneLoop = [
        [0, 0]
    ]
    oneLoop = FrequencyGraph(edgeListOneLoop)
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
    oneTwoLoop = FrequencyGraph(edgeListOneTwoLoop)
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
    oneTwoOne = FrequencyGraph(edgeListOneTwoOne)
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
    oneLoopTwoLoopOne = FrequencyGraph(edgeListOneLoopTwoLoopOne)
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
    oneTwoThreeLoopAndOneThree = FrequencyGraph(edgeListOneTwoThreeLoopAndOneThree)
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
    oneTwoLoopAndThreeTwo = FrequencyGraph(edgeListOneTwoLoopAndThreeTwo)
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
        freq.append(graph.frequencies())
    for ind in range(len(graphList)):
        try:
            for f1,f2 in zip(freq[ind],solutionList[ind]):
                for ff1, ff2 in zip(f1,f2):
                    for val1, val2 in zip(ff1,ff2):
                        if(val1 != val2):
                            assert 0
                        # if not math.isclose(val1,val2, rel_tol=.01):
                        #     assert 0
        except:
            print(freq[ind])
            print(solutionList[ind])
            assert 0, "Frequency Vector did not match test case {0}!".format(graphNames[ind])
        graphList[ind].drawFrequencyGraph(graphNames[ind]+".png")

def main():
    graphTests()
    return

if __name__== "__main__":
  main()
