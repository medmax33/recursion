def odd_from_list(array: list) -> list:
    odd_list: list = []
    return return_odd_from_list(array, odd_list)


def return_odd_from_list(array: list, odd_list: list) -> list:
    # return result in end of array
    if len(array) == 0:
        return odd_list

    # main recursion
    if isinstance(array[0], int) and array[0] % 2 == 0:
        odd_list.append(array[0])
    return return_odd_from_list(array[1:], odd_list)
