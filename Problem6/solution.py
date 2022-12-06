import os

with open('input6.txt', 'r') as f:
    s = f.read()


def find_subroutine(string, checker=4):
    i = 0
    flag = False
    while i<=len(string)-checker and flag==False:
        sub = string[i:i+checker]
        # print(f"Subset is {sub}")
        if len(set(list(sub)))==checker:
            flag = True
            # print(f"Found break at {sub}")
            break
        i += 1
    return i+checker

print("PART ONE")
assert find_subroutine('bvwbjplbgvbhsrlpgdmjqwftvncz')==5
assert find_subroutine('nppdvjthqldpwncqszvftbrmjlhg')==6
assert find_subroutine('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')==10
assert find_subroutine('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')==11
print(find_subroutine(s))

print("PART TWO")
assert find_subroutine('mjqjpqmgbljsphdztnvjfqwrcgsmlb', checker=14)==19
assert find_subroutine('bvwbjplbgvbhsrlpgdmjqwftvncz', checker=14)==23
assert find_subroutine('nppdvjthqldpwncqszvftbrmjlhg', checker=14)==23
assert find_subroutine('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', checker=14)==29
assert find_subroutine('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', checker=14)==26
print(find_subroutine(s, checker=14))