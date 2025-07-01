# has_duplicates.py

def has_duplicates(input_list):
    """
    Checks if the list contains any duplicate values.

    Args:
        input_list: The list to check for duplicates.

    Returns:
        True if duplicates exist, False otherwise.
    """
    n = len(input_list)
    for i in range(n):
        for j in range(i + 1, n):
            if input_list[i] == input_list[j]:
                return True
    return False


if __name__ == "__main__":
    # Example usage:
    list_with_duplicates = [1, 2, 3, 2, 4]
    print(
        f"Does {list_with_duplicates} have duplicates? {has_duplicates(list_with_duplicates)}")

    list_no_duplicates = [1, 2, 3, 4, 5]
    print(
        f"Does {list_no_duplicates} have duplicates? {has_duplicates(list_no_duplicates)}")

    empty_list = []
    print(f"Does {empty_list} have duplicates? {has_duplicates(empty_list)}")

    single_element_list = [7]
    print(
        f"Does {single_element_list} have duplicates? {has_duplicates(single_element_list)}")
