def balanced_parenthesis(number_of_pair: int) -> list:
    result = []
    str_variant = [''] * number_of_pair * 2
    return add_parenthesis(number_of_pair, result, 0, str_variant, 0)


def add_parenthesis(number_of_pair: int, result_list: list, open_minus_close_par: int, str_variant: list, str_index: int) -> list:
    if open_minus_close_par <= number_of_pair * 2 - str_index - 2:
        str_variant[str_index] = '('
        add_parenthesis(number_of_pair, result_list, open_minus_close_par + 1, str_variant, str_index + 1)
    if open_minus_close_par > 0:
        str_variant[str_index] = ')'
        add_parenthesis(number_of_pair, result_list, open_minus_close_par - 1, str_variant, str_index + 1)
    if str_index == number_of_pair * 2 and open_minus_close_par == 0:
        result_list.append(''.join(str_variant))
    return result_list
