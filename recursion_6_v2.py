def return_odd_indexes_values(array: list, array_index: int = 0, result_array: list = []) -> list:
    if len(array) == 0:
        return result_array
    if array_index % 2 == 0:
        result_array.append(array[0])
    return return_odd_indexes_values(array[1:], array_index + 1)
