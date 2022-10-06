#!/usr/bin/env python3

# Warning: Please refrain from using global variables! Your solution will be checked
# by importing your function, not from the raw input/output.

def count_gts_sequences(k: int, p2moves: str, ...) -> int:
    # TO-DO

def gts_wrapper(k: int, p2moves: str) -> int:
    # TO-DO: modify this by "seeding" your initial recursive call
    return count_gts_sequences(k, p2moves, ...)


# DON'T TOUCH the code below
# you can use this helper function for your solution:
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
