def read_file(filepath):
    """
    Reads the input file and separates the values into two lists.
    Returns:
        left_list (list): List of integers from the left column.
        right_list (list): List of integers from the right column.
    """
    left_list, right_list = [], []
    with open(filepath, "r") as file:
        for line in file:
            values = line.strip().split()
            left_list.append(int(values[0]))
            right_list.append(int(values[1]))
    return left_list, right_list


def calculate_abs_difference_score(left_list, right_list):
    """
    Calculates the total score based on the absolute difference 
    between sorted elements of left_list and right_list.
    Returns:
        score (int): Total score based on absolute differences.
    """
    left_list.sort()
    right_list.sort()
    score = sum(abs(left_list[i] - right_list[i]) for i in range(len(right_list)))
    return score


def calculate_similarity_score(left_list, right_list):
    """
    Calculates the similarity score based on occurrences of elements 
    in the right_list multiplied by matching elements in the left_list.
    Returns:
        score (int): Total similarity score.
    """
    # Count occurrences in the right list
    counts = {num: right_list.count(num) for num in right_list}
    # Compute similarity score
    score = sum(left * counts.get(left, 0) for left in left_list)
    return score


def main():
    # Part 1
    left_list, right_list = read_file("/workspaces/Advent-Of-Code-2024/Question1/input.txt")
    abs_difference_score = calculate_abs_difference_score(left_list, right_list)
    print("Absolute Difference Score:", abs_difference_score)
    print("Number of Elements:", len(right_list))

    # Part 2
    similarity_score = calculate_similarity_score(left_list, right_list)
    print("Similarity Score:", similarity_score)


if __name__ == "__main__":
    main()
