def len_with_pop_only(array: list, count: int = 0) -> int:
    try:
        array.pop(0)
    except IndexError:
        return count
    else:
        count += 1
        return len_with_pop_only(array, count)
