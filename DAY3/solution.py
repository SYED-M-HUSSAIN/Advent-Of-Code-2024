import re

def load_data(filepath):
    """
    Loads data from a file and returns it as a string.
    """
    with open(filepath, "r") as file:
        return file.read()

def process_multiplications(data):
    """
    Processes multiplication patterns in the data and computes the score.
    """
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, data)
    score = 0
    for x in matches:
        a = x.replace('mul(', '').replace(')', '').split(',')
        X, Y = map(int, a)
        score += X * Y
    return score

def process_conditional_multiplications(data):
    """
    Processes 'mul', 'do()', and 'don't()' patterns with conditional logic.
    """
    pattern = r"mul\(\d+,\d+\)|\bdo\(\)|\bdon't\(\)"
    matches = re.findall(pattern, data)
    score = 0
    flag = True  # Initially the flag is set to True

    for x in matches:
        if x == "don't()":
            flag = False
            continue
        elif x == "do()":
            flag = True
            continue
        elif flag:
            a = x.replace('mul(', '').replace(')', '').split(',')
            X, Y = map(int, a)
            score += X * Y

    return score

def main():
    # Load the data
    filepath = "/workspaces/Advent-Of-Code-2024/DAY3/input.txt"  # Replace with your actual file path
    data = load_data(filepath)
    
    # Part 1: Process simple multiplications
    score_part1 = process_multiplications(data)
    print(f"Part 1 Score: {score_part1}")

    # Part 2: Process multiplications with conditional logic (do() / don't())
    score_part2 = process_conditional_multiplications(data)
    print(f"Part 2 Score: {score_part2}")

if __name__ == "__main__":
    main()
