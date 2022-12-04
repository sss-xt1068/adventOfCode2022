import pandas as pd
import math
import numpy as np

with open('input1.txt', 'r') as f:
    s = f.read().splitlines()

total = np.array([], dtype='int32')

# Initialization
flag_run = False
sum = 0

# Loop over all lines in input
for line in s:
    # Reset if empty line found
    if line=='':
        total = np.append(total, sum)
        flag_run=False
        sum = 0
        continue
    # Set flag if numbers
    else:
        if flag_run==False:
            flag_run=True
    # Keep summing only if flag set
    if flag_run:
        sum += int(line)

print(f"Maximum of {np.max(total)} found at {np.argmax(total)}")

total_sort = np.sort(total)
print(f"Three highest totals are {np.sum(total_sort[-3:])}")


