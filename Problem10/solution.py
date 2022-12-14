import re
import numpy as np

# with open('test.txt', 'r') as f:
with open('input10.txt', 'r') as f:
    s = f.read().splitlines()

cycle, xval = 1, 1
cycle_dict = {}


for line in s:
    # Case 1: addx V
    # Case 2: noop
    if cycle in {20, 60, 100, 140, 180, 220}:
        print(f"At Cycle {cycle} => {cycle}*{xval} = {cycle*xval}")
        if str(cycle) not in cycle_dict.keys():
            cycle_dict[str(cycle)] = cycle*xval

    # Case 1
    if 'addx' in line:
        # Extract the value to be added 
        V = re.sub('addx ', '', line)
        # Use eval() function to automatically parse the number into V
        V = eval(V)

        # Pre-check for cycle
        if cycle in {20, 60, 100, 140, 180, 220}:
            print(f"At Cycle {cycle} => {cycle}*{xval} = {cycle*xval}")
            if str(cycle) not in cycle_dict.keys():
                cycle_dict[str(cycle)] = cycle*xval

        # Increment cycle to indicate end of addx operation
        cycle += 1

        # Check for cycle
        if cycle in {20, 60, 100, 140, 180, 220}:
            print(f"At Cycle {cycle} => {cycle}*{xval} = {cycle*xval}")
            if str(cycle) not in cycle_dict.keys():
                cycle_dict[str(cycle)] = cycle*xval

        # Finish executing addx operation: update X register
        xval += V

        # Increment cycle to indicate start of next cycle
        cycle += 1

    # If noop operation is found
    elif 'noop' in line:
        # Increment cycle and continue
        cycle += 1
        continue

print(f"\nAnswer to PART 1: {sum(cycle_dict.values())}\n\n")

# ####### PART 2 ##########
cycle, xval = 1, 1
sprite = list(range(xval-1, xval+2))
paint = ""

def match(sprite_arr:list, cycle_val:str):
    ret = None
    if int(cycle_val) in sprite_arr:
        # print("-----Match Found: Drawing a #")
        return '#'
    else:
        # print(f"--------Match not found: {cycle_val} not in {sprite_arr}")
        # print("--------Drawing a .")
        return '.'

print(f"Initially the X register is: {xval}")

sprite = list(range(xval-1, xval+2))
print(f"Initially the sprite is : {sprite}")
print(f"Initially the cycle is at: {cycle}")

last_noop = False

for line in s:
#     # Case 1: addx V
#     # Case 2: noop

#     # Case 1: Cycle 1
    if 'addx' in line:
        # print(f"addx found in instruction: {line}")
        # print(f"Start Cycle\t{cycle}: begin executing {line}")
        # print(f"During Cycle\t{cycle}: CRT draws pixel at position {cycle-1}")
        # draw_char = match(sprite, cycle+1) if last_noop==False else match(sprite, cycle)
        # cycle += 1
        draw_char = match(sprite, (cycle-1)%40)
        paint += draw_char
        # print(f"Current CRT Row: {paint}", end='\n\n')
        V = eval(re.sub('addx ', '', line))
        cycle += 1

        # print(f"During cycle\t{cycle}: CRT draws pixel in position {cycle-1}")
        draw_char = match(sprite, (cycle-1)%40)
        paint += draw_char
        # print(f"Current CRT Row: {paint}")

        xval += V
        # print(f"End of cycle\t{cycle}: finish executing {line} (Register X is now {xval})")
        sprite = list(range(xval-1, xval+2))
        # print(f"Sprite is now at: {sprite}", end='\n\n')

        cycle+=1
        
    elif 'noop' in line:
        # print(f"Start cycle\t{cycle}: begin executing {line}")
        # print(f"CRT draws pixel in position {cycle-1}")

        draw_char = match(sprite, (cycle-1)%40)
        paint += draw_char
        # print(f"Current CRT Row: {paint}")
        # print(f"End of cycle\t{cycle}: finish executing {line}", end='\n\n')
        cycle += 1

print("\nAnswer to PART 2:\n")
paint_np = np.array(list(paint)).reshape(6, 40)
for row in paint_np:
    print(''.join(list(row)))

# EGJBGCFK