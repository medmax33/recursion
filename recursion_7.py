def second_maximum_unit(array: list, max_first: int = None, max_second: int = None) -> int:
    if len(array) == 0:
        return max_second
    if isinstance(array[0], int) is not True:
        return second_maximum_unit(array[1:], max_first, max_second)
    if max_first == max_second:
        max_first = array[0]
        max_second = array[1]
    elif array[0] > max_first:
        max_second = max_first
        max_first = array[0]
    elif max_first > array[0] > max_second:
        max_second = array[0]
    return second_maximum_unit(array[1:], max_first, max_second)
