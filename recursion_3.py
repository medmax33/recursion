def len_with_pop_only(array: list, count: int = 0) -> int:
    if len(array) == 0:
        return count
    else:
        count += 1
        array.pop(0)
        return len_with_pop_only(array, count)
