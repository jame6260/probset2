#!/usr/bin/env python3

# Warning: Please refrain from using global variables! Your solution will be checked
# by importing your function, not from the raw input/output.

def count_gts_sequences(k, p2moves, roundsLeft, numP1, numP2, original, totSeq) -> int:
    p1moves = ['G', 'T', 'S']
    if (roundsLeft == 0):       
        if (numP1 > numP2):
            totSeq.append(numP1)
        p2moves = original
        roundsLeft = k
        numP1 = numP2 = 0
        return

    for j in range(len(p1moves)):
        x = beats(p1moves[j], p2moves[0])
        if (x == 1):
            count_gts_sequences(k, p2moves[1:], roundsLeft-1, numP1+1, numP2, original, totSeq)
        elif (x == 2):   
            count_gts_sequences(k, p2moves[1:], roundsLeft-1, numP1, numP2+1, original, totSeq)
        else:
            count_gts_sequences(k, p2moves[1:], roundsLeft-1, numP1, numP2, original, totSeq)
    return len(totSeq)

def gts_wrapper(k: int, p2moves: str) -> int:
    roundsLeft = k
    numP1 = numP2 = 0
    original = p2moves
    totSeq = []
    return count_gts_sequences(k, p2moves, roundsLeft, numP1, numP2, original, totSeq)

def beats(p1, p2):
    '''
    Given the moves of p1 and p2, it returns:
    * 1 if p1 wins
    * 2 if p2 wins
    * 0 if draw (neither p1 nor p2 wins)
    '''
    table = {'G': {'G': 0, 'T': 1, 'S': 2},
             'T': {'G': 2, 'T': 0, 'S': 1},
             'S': {'G': 1, 'T': 2, 'S': 0}}
    return table[p1][p2]

if __name__ == '__main__':
    k = int(input())
    p2moves = input()
    print(gts_wrapper(k, p2moves))