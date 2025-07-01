# linear_search.py

def linear_search(input_list, target):
    """
    Searches for a target value in the list.

    Args:
        input_list: The list to search within.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise -1.
    """
    for i in range(len(input_list)):
        if input_list[i] == target:
            return i
    return -1


if __name__ == "__main__":
    # Example usage:
    my_list = [10, 20, 30, 40, 50]
    target1 = 30
    print(
        f"Index of {target1} in {my_list}: {linear_search(my_list, target1)}")

    target2 = 60
    print(
        f"Index of {target2} in {my_list}: {linear_search(my_list, target2)}")

    empty_list = []
    target3 = 5
    print(
        f"Index of {target3} in {empty_list}: {linear_search(empty_list, target3)}")

    list_with_duplicates = [1, 5, 2, 5, 3]
    target4 = 5
    print(
        f"Index of {target4} in {list_with_duplicates}: {linear_search(list_with_duplicates, target4)}")
