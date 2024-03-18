def valid_braces(string):
    stack = []
    closes_to_open = ("]", ")", "}")

    for brace in string:
        # check if brace is a closing one
        if brace in closes_to_open:
            # brace has an equivalent closing brace in the stack
            closing_brace = stack.pop()
            if brace is not closing_brace:
                return False        
             
        else:
            if brace == "(":
                stack.append(")")
            if brace == "{":
                stack.append("}")
            if brace == "[":
                stack.append("]")
    return True


