from collections import Counter, defaultdict


class Solution:

    def smallest_distinct_window(self, s: str) -> int:
        freq_counter = defaultdict(int)
        left = 0
        unique_chars = set(s)
        substring_set = set()
        length = len(unique_chars)
        min_length = float("inf")

        for index, letter in enumerate(s):
            # we shall keep tabs on all letters and their counts
            freq_counter[letter] += 1

            # add the current letter to substring_set
            substring_set.add(letter)

            # check if the two sets are equal
            while len(substring_set) == length:
                # if they are then we should trim the window
                # such that we have all letters, but window is at minimum length
                window = index - left + 1
                min_length = min(min_length, window)
                left_char = s[left]
                # we remove the left char from our freq_counter
                freq_counter[left_char] -= 1
                # check to see if left char count is at zero
                if freq_counter[left_char]  == 0:
                    # we then remove from our sub string set
                    substring_set.remove(left_char)
                left += 1

        return min_length


if __name__ == "__main__":
    print(Solution().smallest_distinct_window("aaab"))
