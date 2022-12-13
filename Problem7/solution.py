import pandas as pd
import re
from itertools import combinations

with open('input7.txt', 'r') as f:
# with open('test.txt', 'r') as f:
    # Do not include first line
    s = f.read().splitlines()[1:]

# sub = s[:100]
sub = s
file_system = {}
cur_path = ''
parent_path = None
cur_file = None
file_sum = 0
list_flag = False


for index, line in enumerate(sub):
    # Case 1: cd command moving down a directory
    # Case 2: cd command moving up a level
    # Case 3: ls command for listing contents
    # Case 4: Actual list entry with a directory name
    # Case 5: Actual list entry with a size and file name

    if '$ cd' in line:
        # print(f"$$$$$$$ Currently at {cur_path} $$$$$$")
        if cur_path not in file_system.keys():
            # print(f"{index+2}   {cur_path}: Total so far: {file_sum}")
            file_system[cur_path] = file_sum

        list_flag = False

    # Case 2:
    if line=='$ cd ..':
        parent_path = cur_path
        cur_path = re.sub(r'\/\w+$', '', cur_path)
        file_sum = 0
        # print(f"Moving UP from {parent_path} --> {cur_path}")

        continue
    # Case 1:
    elif '$ cd' in line:
        path = line.replace('$ cd ', '').strip()
        # print(f"###### Resetting file_sum at {path} #####")
        parent_path = cur_path
        cur_path = f"{cur_path}/{path}"
        file_sum = 0
        # print(f"Moving from {parent_path} --> {cur_path}")
        continue

    # Case 3:
    elif '$ ls' in line:
        # print("Listing now..")
        list_flag = True
        continue

    # Case 4: List entry for directory
    elif 'dir ' in line:
        # print("Found directory listing")
        continue

    # Case 5:
    else:
        # print("Possibly file listing")
        if list_flag:
            file_sum += eval(line.split(' ')[0])

    # print(index, '\t', file_sum, end='^^^^^^^^^\n')

# print(parent_path, cur_path)
file_system[cur_path] = file_sum

# Dictionary now ready to loop over
# for k,v in file_system.items():
#     print(f"{k}: {v}")

all_keys = list(file_system.keys())
# all
file_system_copy = file_system.copy()


for k1 in all_keys:
    for k2 in all_keys:
        if k1!=k2 and k1 in k2:
            # print(f"Found subset {k1} inside {k2}")
            file_system_copy[k1] += file_system_copy[k2]

df = pd.DataFrame(data = file_system_copy.values(),
index=file_system_copy.keys())
df.columns = ['total']
df.reset_index(inplace=True)
df2 = df.copy()
df.sort_values(by='total', ascending=False, inplace=True)

df1 = df[df['total']<=100000]
# print("DF")
# print(df.head())
# print("DF1")
# print(df1.head())
print(f"Answer to Part 1: {df1['total'].sum()}")