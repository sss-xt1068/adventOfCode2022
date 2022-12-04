import pandas as pd
import numpy as np

with open('input2.txt', 'r') as f:
    s = f.read().splitlines()

df = pd.DataFrame(s, columns=['base'])

lose_moves = {'A': 'Z', 'B': 'X', 'C': 'Y'}
win_moves = {'A': 'Y', 'B': 'Z', 'C': 'X'}
draw_moves = {'A':'X', 'B':'Y', 'C': 'Z'}

# Part 2
def find_move(ms_tuple):
    """
    Args:
        ms_tuple: A tuple of the opponents move and decided outcome

    Returns:
        string variable defining the move that should be chosen 
    """
    opp_move, outcome = ms_tuple
    if outcome == 0:
        return lose_moves[opp_move]
    elif outcome==0.5:
        return draw_moves[opp_move]
    else:
        return win_moves[opp_move]

def decide_winner(action_tuple):
    """
    Args:
        action_tuple : tuple
        - First element defines the action by opponent
        - Second element defines the action by you

    Returns:
    winner : integer that defines if outcome is win, loss, or draw
    - 1 if you win
    - 0 if you lose
    - 0.5 if draw
    """
    left, right = action_tuple
    # print(left, right)
    if left in ['A', 'X']:
        if right in ['C', 'Z']:
            return 0
        elif right in ['B', 'Y']:
            return 1
        else:
            return 0.5
    elif left in ['B', 'Y']:
        if right in ['A', 'X']:
            return 0
        elif right in ['C', 'Z']:
            return 1
        else:
            return 0.5
    elif left in ['C', 'Z']:
        if right in ['A', 'X']:
            return 1
        elif right in ['B', 'Y']:
            return 0
        else:
            return 0.5


# Part 1
df['opp'] = df['base'].apply(lambda x: x.split(' ')[0])
df['move1'] = df['base'].apply(lambda x: x.split(' ')[1])

# Move score: 1, 2, or 3
df['move_score1'] = df['move1'].replace({'X': 1, 'Y': 2, 'Z': 3})
df['win_score1'] = 6 * df[['opp', 'move1']].apply(decide_winner, axis=1)
df['final_score1'] = df['move_score1'] + df['win_score1']

print(int(sum(df['final_score1'])))

# Part 2
df['win_score2'] = df['move1'].replace({'X': 0, 'Y': 0.5, 'Z':1})
df['move2'] = df[['opp', 'win_score2']].apply(find_move, axis=1)
df['win_score2'] = 6*df['win_score2']
df['move_score2'] = df['move2'].replace({'X': 1, 'Y': 2, 'Z': 3})
df['final_score2'] = df['win_score2'] + df['move_score2']
print(df['final_score2'].sum())