def read_file(file_path):
    """Reads the file and returns its lines."""
    with open(file_path, 'r') as file:
        return file.readlines()

def process_pairs(lines):
    """Processes the lines to extract pairs."""
    pair = []
    for line in lines:
        if '|' in line:
            pair.append(line.strip())  # Add each pair as a string
    return pair

def process_had(lines):
    """Processes the lines to extract 'had' arrays."""
    had = []
    current_had = []
    for line in lines:
        if '|' not in line and ',' in line:  # Detect "had" lines
            numbers = list(map(int, line.strip().split(',')))  # Convert to integers
            current_had.append(numbers)
    had = current_had  # Assign processed "had" arrays
    return had

def calculate_val(had, pair, flag_condition):
    """Calculates the middle values based on the flag condition."""
    val = []
    for x in had:
        flag = True
        count = 0
        for y in x:
            if flag:
                for v in range(count+1, len(x)):
                    a = f"{y}|{x[v]}"
                    if a not in pair:
                        flag = False
                        break
                count += 1
            else:
                break
        if flag_condition(flag):
            # Find the middle element(s)
            length = len(x)
            if length % 2 == 1:  # Odd length
                middle = x[length // 2]
            val.append(middle)
    return val

def main():
    # File path
    file_path = '/Users/beam/Downloads/test/input.txt'

    # Read the file
    lines = read_file(file_path)

    # Process pairs and 'had' arrays
    pair = process_pairs(lines)
    had = process_had(lines)

    # Calculate the first value (where flag is True)
    val = calculate_val(had, pair, lambda flag: flag)
    print(sum(val))

    # Calculate the second value (where flag is False)
    val = calculate_val(had, pair, lambda flag: not flag)
    print(sum(val))

if __name__ == "__main__":
    main()
