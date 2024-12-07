from itertools import chain
class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringify = str(x)
        length = len(stringify)
        left = 0
        right = length - 1

        while left <= (length // 2):
            left_character = stringify[left]
            right_character = stringify[right]
            left += 1
            right -= 1
            if left_character != right_character:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(321))

