from typing import List


class Solution:

    def longest_common_prefix(self, strs: List[str]) -> str:
        # strings are expected to be less than 200 in length
        min_length = 201
        i = 0
        for word in strs:
            if len(word) < min_length:
                min_length = len(word)

        while i < min_length:
            for word in strs:
                #compare each letter with letters from 1st element in strs

                if word[i] != strs[0][i]:
                    return word[:i]
            i += 1

        return word[:i]


if __name__ == "__main__":
    print(Solution().longest_common_prefix(["flower", "flow", "flight"]))
    print(Solution().longest_common_prefix(["aa", "aa"]))
    print(Solution().longest_common_prefix([""]))

