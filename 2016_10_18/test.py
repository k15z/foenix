import unittest
from copy import deepcopy

ready = True
if ready:
    from code import SudokuNode
else:
    from solution import SudokuNode

n = [[None]*3 for _ in range(3)]

n[0][0] = SudokuNode(3, {1:0.8,2:0.1,3:0.1})
n[0][1] = SudokuNode(3, {1:0.6,2:0.3,3:0.1})
n[0][2] = SudokuNode(3)

n[1][0] = SudokuNode(3)
n[1][1] = SudokuNode(3)
n[1][2] = SudokuNode(3)

n[2][0] = SudokuNode(3)
n[2][1] = SudokuNode(3)
n[2][2] = SudokuNode(3)

n[0][0].add(n[0][1]).add(n[0][2])
n[0][1].add(n[0][2])
n[1][0].add(n[1][1]).add(n[1][2])
n[1][1].add(n[1][2])
n[2][0].add(n[2][1]).add(n[2][2])
n[2][1].add(n[2][2])

n[0][0].add(n[1][0]).add(n[2][0])
n[1][0].add(n[2][0])
n[0][1].add(n[1][1]).add(n[2][1])
n[1][1].add(n[2][1])
n[0][2].add(n[1][2]).add(n[2][2])
n[1][2].add(n[2][2])

import random
for _ in range(100):
    i = random.randint(0, 2) 
    j = random.randint(0, 2) 
    n[i][j].send()

def get_max(node):
    return max([(node.dist[key], key) for key in node.dist.keys()])[1]

print(get_max(n[0][0]), get_max(n[0][1]), get_max(n[0][2]))
print(get_max(n[1][0]), get_max(n[1][1]), get_max(n[1][2]))
print(get_max(n[2][0]), get_max(n[2][1]), get_max(n[2][2]))
