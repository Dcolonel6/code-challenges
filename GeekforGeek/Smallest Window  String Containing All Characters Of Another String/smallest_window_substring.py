# User function Template for python3
from collections import defaultdict, Counter


# Function to find the smallest window in the string s1 consisting
# of all the characters of string s2.
class Solution:
    def min_window(self, s1: str, s2: str) -> str:
        # code here
        s2_counter = Counter(s2)
        freq_counter = defaultdict(int)
        left = 0
        matches = 0
        smallest_substr = ""
        smallest_window = float("inf")

        for right, letter in enumerate(s1):
            # check if current letter is in s2_counter
            if letter in s2_counter:
                # add it to the freq_counter
                freq_counter[letter] += 1
                # check if we have filled the key
                if freq_counter[letter] == s2_counter[letter]:
                    # increase matches. Will track whether we have all chars
                    # in s2. If we do, the len(s2_counter) == matches
                    matches += 1

            while len(s2_counter) == matches and left <= right:
                left_char = s1[left]
                window = right - left + 1
                # check if letter is in s2_counter
                if left_char in s2_counter:
                    # remove it from freq_counter
                    freq_counter[left_char] -= 1

                    # have we reduced the count to the point it affects our matches?
                    if freq_counter[left_char] < s2_counter[left_char]:
                        # yes we have and now we should decrease our matches
                        matches -= 1
                # get the smallest substr and window
                if window < smallest_window:
                    smallest_substr = s1[left:right + 1]
                    smallest_window = window
                left += 1

        return smallest_substr


if __name__ == "__main__":
    print(Solution().min_window("c",  ""))
