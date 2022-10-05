def main_second_maximum_unit(array: list) -> int:
    if len(array) < 2:
        return array[0]
    max_first: int = None
    max_second: int = None
    return second_maximum_unit(array, max_first, max_second)


def second_maximum_unit(array: list, max_first: int = None, max_second: int = None) -> int:
    # return result in end of array
    if len(array) == 0:
        return max_second

    # compare array[0], max_first, max_second
    if max_first == max_second:
        max_first = array[0]
        max_second = array[1]
    elif array[0] > max_first:
        max_second = max_first
        max_first = array[0]
    elif max_first > array[0] > max_second:
        max_second = array[0]

    # main recursion
    return second_maximum_unit(array[1:], max_first, max_second)
