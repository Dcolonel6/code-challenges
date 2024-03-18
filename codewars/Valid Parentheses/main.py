def valid_parentheses(paren_str):
    while "()" in paren_str:
        paren_str = paren_str.replace("()", "")
    return paren_str == ""