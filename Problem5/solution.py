import os
import math
import time
import re
import pandas as pd

# with open('input5.txt', 'r') as f:
with open('input5.txt', 'r') as f:
    s = f.read().splitlines()

k1 = ['D', 'T', 'W', 'F', 'J', 'S', 'H', 'N']
k2 = ['H', 'R', 'P', 'Q', 'T', 'N', 'B', 'G']
k3 = ['L', 'Q', 'V']
k4 = ['N', 'B', 'S', 'W', 'R', 'Q']
k5 = ['N', 'D', 'F', 'T', 'V', 'M', 'B']
k6 = ['M', 'D', 'B', 'V', 'H', 'T', 'R']
k7 = ['D', 'B', 'Q', 'J']
k8 = ['D', 'N', 'J', 'V', 'R', 'Z', 'H', 'Q']
k9 = ['B', 'N', 'H', 'M', 'S']
grid = [k1, k2, k3, k4, k5, k6, k7, k8, k9]

# k1 = ['Z', 'N']
# k2 = ['M', 'C', 'D']
# k3 = ['P']
# grid = [k1, k2, k3]

# grid_len = 5
grid_len = 10

def showgrid(grid, message=''):
    print(f"### Current Grid:{message} ###")
    for line in grid:
        print(line)
    print("########### END ###############")

moves = s[grid_len:]
for move in moves:
    numbers = [int(x) for x in re.findall('\d+', move)]
    n, src, dest = numbers
    print(f"Moving {n} from array {src} to array {dest}")
    
    # # Stack behaviour: Part 1
    # for _ in range(n):
    #     pick = grid[src-1].pop()
    #     print(f"Picked {pick} at {numbers}")
    #     grid[dest-1].extend([pick])
    #     showgrid(grid, message=f"{numbers}")

    # Queue behaviour: Part 2
    tail = grid[src-1][-1*n:]
    grid[src-1] = grid[src-1][:-1*n]
    grid[dest-1].extend(tail)


showgrid(grid, message="Final")

# for stack in grid:
#     print(stack[-1])