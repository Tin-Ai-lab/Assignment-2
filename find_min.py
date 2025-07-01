# find_min.py

def find_min(input_list):
    """
    Finds the smallest number in a list.

    Args:
        input_list: The list of numbers.

    Returns:
        The smallest number in the list, or None if the list is empty.
    """
    if not input_list:
        return None

    min_value = input_list[0]
    for element in input_list:
        if element < min_value:
            min_value = element
    return min_value


if __name__ == "__main__":
    # Example usage:
    my_list = [1, 2, 3, 4, 5]
    print(f"The minimum element in {my_list} is: {find_min(my_list)}")

    empty_list = []
    print(f"The minimum element in {empty_list} is: {find_min(empty_list)}")

    single_element_list = [42]
    print(
        f"The minimum element in {single_element_list} is: {find_min(single_element_list)}")

    negative_list = [-10, -2, -8]
    print(
        f"The minimum element in {negative_list} is: {find_min(negative_list)}")
