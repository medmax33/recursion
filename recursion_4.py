def is_string_palindrom(string: str) -> bool:
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] == string[-1]:
        return is_string_palindrom(string[1:-1])
    else:
        return False
