import re # for regular expression searching

# with open('test.txt', 'r') as f: # For reading test input
with open('input11.txt', 'r') as f: # Fore reading actual input
    inp = [x.splitlines() for x in f.read().split('\n\n')] # Split monkeys

monkeys = {} # Global dictionary to maintain monkeys' information

def parse_function(operation):
    """
    Args:
        operation: string
        This defines the new calculation in terms of the old value
    Returns:
        lambda function in terms of the old value as a parameter x
    """
    op = re.sub('  Operation: new = ', '', operation)
    if 'old * old' in op:
        # Special case: Square of old value
        return lambda x: x*x
    op2 = re.sub('old', '100', op)
        # Case 1: Multiplicative
    return (lambda x: x * (eval(op2) // 100)) if '*' in op2 else \
    (lambda x: x + (eval(op2) - 100)) # Case 2: Additive

def parse_test(test):
    """
    Args:
        test: string that defines the divisibility test for the monkey
    Returns:
        a numerical value of the identified divisor and
        a lambda function that can test for the divisibility of the passed number
    """
    test = int(re.sub('  Test: divisible by ', '', test))
    return test, lambda x: x%test==0

def parse_path(l):
    """
    Args:
        l: a list of 2 elements containing targets based on result of test
    Returns:
        cond_true: Monkey to pass to if test is true
        cond_false: Monkey to pass to if test is false
    """
    cond_true, cond_false = l
    cond_true = re.findall('\d+', cond_true)[0]
    cond_false = re.findall('\d+', cond_false)[0]
    return (cond_true, cond_false)


def list_monkey(monkey):
    """
    Args:
        monkey: list of 5 strings containing name of the monkey, initial
        items held, operation function for worry level, divisibility test,
        and monkey to pass to based on result of divisibility test
    Returns: None
    """
    global monkeys
    # mname = re.sub('Monkey ', '', name)
    m_name = re.findall('(\d+):', monkey[0])[0] # Name of monkey
    m_items = re.findall('\d+', monkey[1])      # Initial items
    m_oper = parse_function(monkey[2])          # Operation function
    m_divisor, m_test = parse_test(monkey[3])              # Test condition
    m_true, m_false = parse_path(monkey[4:])
    # print(m_name)
    # print(m_items)
    # print(m_func)
    # print(m_test)
    monkeys.setdefault(m_name,
     {'items': [int(x) for x in m_items],
     'test': m_test,
     'function': m_oper,
     'test': m_test,
     'true_pass': m_true,
     'false_pass': m_false,
     'divisor': m_divisor,
     'count': 0
     }
    )

# Part 2 ONLY
def find_common_divisor(m_list):
    """
    Args:
        Dictionary with information on every monkey
    Returns:
        One common divisor that is a multiple of all the divisors
    """
    
    div = 1
    for monkey in m_list.keys():
        div = div * monkeys[monkey]['divisor']
    return div

# Initialize all monkeys as dictionary
for monkey in inp:
    list_monkey(monkey)

# Define the number of rounds for which game runs
nrounds = 10000
# nrounds = 20

common_divisor = find_common_divisor(monkeys)

# For every round
for round in range(nrounds):

    # Loop over all monkeys
    for monkey, info in monkeys.items():

        # Loop over all items currently held by them
        for item in info['items']:

            # Find new worry level based on the calculation 
            new_worry = info['function'](item)

            # Drop worry level as per instruction: Part 1 ONLY
            # new_worry = new_worry//3

            # Drop worry level by taking modulus with the common divisor: Part 2 ONLY
            new_worry = new_worry%common_divisor

            # Test for divisibility and save as boolean
            worry_status = info['test'](new_worry)

            # Decide the monkey to pass to based on worry_status
            pass_to = info['true_pass'] if worry_status else info['false_pass']

            # Pass to correct monkey: append to their list of items
            monkeys[pass_to]['items'].append(new_worry)

            info['count'] += 1
            # print(f"\tItems evaluated: {info['count']}\n\tPassed on to monkey {pass_to}")

        # Empty the list of items at the end of round for that monkey
        info['items'] = []

# Display comparisons made by each monkey at the end of all rounds
for k, v in monkeys.items():
    print(f"Comparisons made by monkey {k}: {v['count']}")

print("#"*79)
# Find top two busiest monkeys
sorted_monkeys = sorted(monkeys.items(), key=lambda item: item[1]['count'])
top = sorted_monkeys[-2:]
top_comp = [str(x[1]['count']) for x in top]
# print(top_comp)

print(f"Answer: {eval('*'.join(top_comp))}")