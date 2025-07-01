# sum_of_elements.py

def sum_of_elements(input_list):
    """
    Calculates the sum of all values in a list.

    Args:
        input_list: The list of numbers.

    Returns:
        The sum of all elements in the list.
    """
    total_sum = 0
    for element in input_list:
        total_sum += element
    return total_sum


if __name__ == "__main__":
    # Example usage:
    my_list = [1, 2, 3, 4, 5]
    print(f"The sum of elements in {my_list} is: {sum_of_elements(my_list)}")

    empty_list = []
    print(
        f"The sum of elements in {empty_list} is: {sum_of_elements(empty_list)}")

    negative_list = [-1, -2, -3]
    print(
        f"The sum of elements in {negative_list} is: {sum_of_elements(negative_list)}")
