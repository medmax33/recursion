def main_second_maximum_unit(array: list) -> int:
    if len(array) < 2:
        return array[0]
    if array[0] > array[1]:
        max_first: int = array[0]
        max_second: int = array[1]
    else:
        max_first: int = array[1]
        max_second: int = array[0]
    current_index: int = 1
    return second_maximum_unit(array, current_index, max_first, max_second)


def second_maximum_unit(array: list, current_index: int, max_first: int, max_second: int) -> int:
    # return result in end of array
    if current_index > len(array) - 1:
        return max_second

    # compare array[0], max_first, max_second
    if array[current_index] > max_first:
        max_second = max_first
        max_first = array[current_index]
    elif max_first > array[current_index] > max_second:
        max_second = array[current_index]

    # main recursion
    return second_maximum_unit(array, current_index + 1, max_first, max_second)
