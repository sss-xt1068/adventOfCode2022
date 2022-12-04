import pandas as pd
import numpy as np
import time

with open('input3.txt', 'r') as f:
    s = f.read().splitlines()

def build_priorities():
    """
    Returns:
        Dictionary of priorities for every character as decided
    """
    final_p = {chr(i+96):i for i in range(1, 27)}
    high_p = {chr(i+64):i+26 for i in range(1, 27)}
    final_p |= high_p
    return final_p

map_p = build_priorities()   # Load all priorities as dictionary

def find_priority(x):
    """
    Args:
        x: list of characters for which to find priorities
    Returns:
        sum of priorities of all characters in x
    """
    psum = [map_p[char] for char in x]
    return sum(psum)

def find_sum(x):
    """
    Args:
        x: List of three consecutive elf's packages
    Returns:
        The priority of the common sticker representing the packages
    """
    s1, s2, s3 = set(list(x[0])), set(list(x[1])), set(list(x[2]))
    sticker = list(s1.intersection(s2).intersection(s3))[0]
    # print(sticker)
    return map_p[sticker]

# Build basic dataframes
df = pd.DataFrame(s, columns=['base'])

# Separate the left and right compartments
df['c1'] = df['base'].apply(lambda x: x[:len(x)//2])
df['c2'] = df['base'].apply(lambda x: x[len(x)//2:])

# Find the common items in left and right compartments
df['uniq'] = df[['c1', 'c2']].apply(lambda x: set(list(x[0])).intersection(set(list(x[1]))), axis=1)

tick = time.time()

df['prior'] = df['uniq'].apply(find_priority)
tock = time.time()
print(f"Time taken in seconds: {round(tock-tick, 4)}")

print(f"Part 1: {df['prior'].sum()}")

group_sum = []
for rown in range(df.shape[0]//3):
    subset = df.iloc[rown*3:rown*3 + 3]
    l1 = list(subset['base'].values)
    group_sum.append(find_sum(l1))

print(f"Part 2: {sum(group_sum)}")