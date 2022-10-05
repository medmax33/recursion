def return_odd_indexes_values(array: list, array_index: int = 0, result_array: list = None) -> list:
    # define result array
    if result_array is None:
        result_array = []

    # return result in end of array
    if len(array) == 0:
        return result_array

    # main recursion
    if array_index % 2 == 0:
        result_array.append(array[0])
    return return_odd_indexes_values(array[1:], array_index + 1)
