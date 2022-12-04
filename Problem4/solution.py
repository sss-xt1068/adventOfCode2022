import pandas as pd
import numpy as np
import time

with open('input4.txt', 'r') as f:
    s = f.read().splitlines()

# Part 1
def find_range(c):
    s1, e1 = c.split(',')[0].split('-')
    s2, e2 = c.split(',')[1].split('-')
    s1, e1, s2, e2 = int(s1), int(e1), int(s2), int(e2)
    if (s1<=s2 and e1>=e2):
        return True
    elif (s1>=s2 and e1<=e2):
        return True
    else:
        return False

# Part 2
def find_overlap(c):
    s1, e1 = c.split(',')[0].split('-')
    s2, e2 = c.split(',')[1].split('-')
    s1, e1, s2, e2 = int(s1), int(e1), int(s2), int(e2)
    r1 = list(range(s1, e1+1))
    r2 = list(range(s2, e2+1))
    if len(set(r1).intersection(set(r2)))>0:
        return True
    else: return False


df = pd.DataFrame(s, columns=['base'])

df['intersect'] = df['base'].apply(find_range)
df['overlap'] = df['base'].apply(find_overlap)

print(f"Part 1: {df['intersect'].sum()}")
print(f"Part 2: {df['overlap'].sum()}")