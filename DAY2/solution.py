def load_data(filepath):
    """
    Loads data from a file and returns it as a list of integer lists.
    """
    meta_data = []
    with open(filepath, "r") as file:
        for line in file:
            values = line.strip().split()
            meta_data.append([int(x) for x in values])
    return meta_data

def count_unsafe_reports(meta_data):
    """
    Counts the number of unsafe reports based on the given rules.
    """
    count_unsafe = 0
    for x in meta_data:
        if x[0] < x[-1]:
            for y in range(len(x) - 1):
                if x[y] + 3 >= x[y + 1] and x[y] != x[y + 1] and x[y] < x[y + 1]:
                    continue
                else:
                    count_unsafe += 1
                    break
        else:
            for y in range(len(x) - 1):
                if x[y] - 3 <= x[y + 1] and x[y] != x[y + 1] and x[y] > x[y + 1]:
                    continue
                else:
                    count_unsafe += 1
                    break
    return count_unsafe

def is_safe(sequence):
    """
    Checks if a sequence is safe according to the rules.
    """
    if all(x < y for x, y in zip(sequence, sequence[1:])):  # Check increasing
        return all(1 <= y - x <= 3 for x, y in zip(sequence, sequence[1:]))
    if all(x > y for x, y in zip(sequence, sequence[1:])):  # Check decreasing
        return all(1 <= x - y <= 3 for x, y in zip(sequence, sequence[1:]))
    return False

def is_safe_with_dampener(sequence):
    """
    Checks if a sequence is safe or can be made safe by removing one level.
    """
    if is_safe(sequence):
        return True
    # Try removing each level and check if the modified sequence is safe
    for i in range(len(sequence)):
        modified_sequence = sequence[:i] + sequence[i + 1:]
        if is_safe(modified_sequence):
            return True
    return False


def count_safe_reports(meta_data):
    """
    Counts the number of safe reports based on the dampener rule.
    """
    safe_count = 0
    for report in meta_data:
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count

# Main code execution
if __name__ == "__main__":
    filepath = "/workspaces/Advent-Of-Code-2024/DAY2/input.txt"
    
    # Load data
    meta_data = load_data(filepath)
    
    # Part 1: Count unsafe reports
    unsafe_count = count_unsafe_reports(meta_data)
    print(f"Safe reports count (Part 1): {len(meta_data) - unsafe_count}")
    
    # Part 2: Count safe reports with dampener
    safe_count = count_safe_reports(meta_data)

    print(f"Number of safe reports (Part 2): {safe_count}")
