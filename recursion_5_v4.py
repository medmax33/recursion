def odd_from_list(array: list) -> list:
    odd_list: list = []
    current_index = 0
    return return_odd_from_list(array, current_index, odd_list)


def return_odd_from_list(array: list, current_index: int, odd_list: list) -> list:
    # return result in end of array
    if current_index > len(array) - 1:
        return odd_list

    # main recursion
    if isinstance(array[current_index], int) and array[current_index] % 2 == 0:
        odd_list.append(array[current_index])
    return return_odd_from_list(array, current_index + 1, odd_list)
