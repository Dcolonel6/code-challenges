

class Solution:
    def is_valid(self,s:str):
        pairs = {")":"(", "}": "{", "]":"["}
        stack = []

        for bracket in s:
            # check if its an opening bracket
            if bracket not in pairs:
                # it's an opening bracket, add to stack
                stack.append(bracket)
            else:
                # check if stack not empty?
                if stack:
                    matching_opening_brakect = stack.pop()
                    if  matching_opening_brakect != pairs[bracket]:
                        return False
                else:
                    # we have too many closing brackets
                    return False
        return False if stack else True

if __name__ == "__main__":
    print(Solution().is_valid("]"))