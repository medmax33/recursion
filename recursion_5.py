def return_odd_from_list(array: list, result_array: list = []) -> list:
    if len(array) == 0:
        return result_array
    current_unit = array.pop(0)
    if isinstance(current_unit, int) and current_unit % 2 == 0:
        result_array.append(current_unit)
    return return_odd_from_list(array, result_array)
