import numpy as np
def evalMoves(target, legalMoves):
    allDist = []
    for move in legalMoves:
        dist = np.linalg.norm(target - move)
        allDist.append(dist)
    bestMove = legalMoves[np.argmin(allDist)]
    return(bestMove)



