# find_max.py

def find_max(input_list):
    """
    Finds the largest number in a list.

    Args:
        input_list: The list of numbers.

    Returns:
        The largest number in the list, or None if the list is empty.
    """
    if not input_list:
        return None

    max_value = input_list[0]
    for element in input_list:
        if element > max_value:
            max_value = element
    return max_value


if __name__ == "__main__":
    # Example usage:
    my_list = [1, 2, 3, 4, 5]
    print(f"The maximum element in {my_list} is: {find_max(my_list)}")

    empty_list = []
    print(f"The maximum element in {empty_list} is: {find_max(empty_list)}")

    single_element_list = [42]
    print(
        f"The maximum element in {single_element_list} is: {find_max(single_element_list)}")

    negative_list = [-10, -2, -8]
    print(
        f"The maximum element in {negative_list} is: {find_max(negative_list)}")
