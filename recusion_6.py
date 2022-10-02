def return_odd_indexes_values(array: list, array_index: int = 0, result_array: list = []) -> list:
    if len(array) == 0:
        return result_array
    current_item = array.pop(0)
    if array_index % 2 == 0:
        result_array.append(current_item)
    return return_odd_indexes_values(array, array_index + 1)
