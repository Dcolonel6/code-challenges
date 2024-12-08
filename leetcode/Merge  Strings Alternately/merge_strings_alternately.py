from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined_string = ""

        for (x, y) in  zip_longest(word1, word2, fillvalue="*"):
            if x.isalpha():
                combined_string += x
            if y.isalpha():
                combined_string += y
        return combined_string




if __name__ == "__main__":
    print(Solution().mergeAlternately("ab", "pqrs"))
