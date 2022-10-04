def return_odd_from_list(array: list, result_array: list = []) -> list:
    if len(array) == 0:
        return result_array
    if isinstance(array[0], int) and array[0] % 2 == 0:
        result_array.append(array[0])
    return return_odd_from_list(array[1:], result_array)
