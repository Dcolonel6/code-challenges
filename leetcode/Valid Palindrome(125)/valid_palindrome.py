import re


"""
    A phrase is a palindrome if, after converting all uppercase letters into 
    lowercase letters and removing all non-alphanumeric characters, it reads 
    the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        sanitized_s = re.findall(r"[a-z0-9]", s_lower)
        index = 0
        sanitized_length = len(sanitized_s)
        right = sanitized_length - 1
        if sanitized_length <= 1:
            return True
        if sanitized_length == 2:
            return sanitized_s[index] == sanitized_s[right]

        while index <= right:
            letter_index = sanitized_s[index]
            letter_right = sanitized_s[right]

            if letter_index != letter_right:
                return False

            index += 1
            right -= 1

        return True


if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
