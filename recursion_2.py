def summ_of_digits(n: int) -> int:
    if n < 0:
        n = -n
    m = n % 10
    n = n // 10
    if n != 0:
        return m + summ_of_digits(n)
    else:
        return m
