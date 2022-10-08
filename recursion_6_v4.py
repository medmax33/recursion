def odd_indexes_values(array: list) -> list:
    array_index: int = 0
    result_array: list = []
    return return_odd_indexes_values(array, array_index, result_array)


def return_odd_indexes_values(array: list, array_index: int, result_array: list) -> list:
    # return result in end of array
    if array_index > len(array) - 1:
        return result_array

    # main recursion
    if array_index % 2 == 0:
        result_array.append(array[array_index])
    return return_odd_indexes_values(array, array_index + 1, result_array)
