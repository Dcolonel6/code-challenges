
class Solution:
    def make_remove_invalid(self, s:str) -> str:
        left_parentheses = 0
        right_parentheses = 0

        string_builder = []

        for char in s:
            # check if its a leftie, we will be greedy and
            # accepts them all
            if char == "(":
                left_parentheses += 1
                string_builder.append(char)
            if char == ")":
                # only accept them under the condition that
                # left_parentheses is > right_parentheses, discard otherwise
                if left_parentheses > right_parentheses:
                    right_parentheses += 1
                    string_builder.append(char)
            if char != ")" and char != "(":
                # accept anything thats not a parentheses
                string_builder.append(char)

        # if left_parentheses and right_parentheses are equal, then we have balanced everything
        result = "".join(string_builder)
        if left_parentheses == right_parentheses:
            return result
        else:
            # we have too many opening parentheses and need to discard them
            # we shall be greedy with closing parentheses and selective with opening ones
            for letter in string_builder[::-1]:
                if char == ")":
                    pass