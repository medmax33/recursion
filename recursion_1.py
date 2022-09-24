def exponentiation_n_to_m(n: int, m: int) -> float:
    if m < 0:
        m = -m
        return 1 / (n * exponentiation_n_to_m(n, m - 1))
    if m == 0:
        return 1
    if m == 1:
        return n
    return n * exponentiation_n_to_m(n, m - 1)
