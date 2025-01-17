from collections import Counter, defaultdict


class Solution:
    def minimum_window(self, s: str, t: str) -> str:
        freq_counter = Counter(t)
        left = 0
        right = 0
        min_window = float("inf")
        length = len(s)
        sub_ary_counter = defaultdict(int)
        matches = 0 # tracks matches
        smallest_sub = ""

        # if length == 1 and len(t) == 1 and s[0] == t[0]:
        #     return smallest_sub

        while right < length:
            current_letter = s[right]
            if current_letter in freq_counter:
                # increase only if they are in t
                sub_ary_counter[current_letter] += 1
                # after increment, check if the letter is the same in both sub_ary_counter and freq_counter
                if sub_ary_counter[current_letter] == freq_counter[current_letter]:
                    # if they are increase match
                    matches += 1

            # if matches is eq to length of of freq_counter
            # and left <= right

            while matches == len(freq_counter) and left <= right:
                left_letter = s[left]
                # is the letter part of t ?
                if left_letter in sub_ary_counter:
                    # we should decrease both the matches and the frequency count in sub_ary_counter
                    sub_ary_counter[left_letter] -= 1
                    # we only decrease the match counter only if the frequency of that specific letter
                    # in sub_ary_counter is less than the desired outcome in t
                    if sub_ary_counter[left_letter] < freq_counter[left_letter]:
                        matches -= 1

                # window length is
                window = right - left + 1
                # compares the length of previous sub ary window with current one and chooses the smaller
                # also caches the smallest sub
                if window < min_window:
                    min_window = window
                    smallest_sub = s[left: right+1]
                left += 1
            right += 1
        return smallest_sub


if __name__ == "__main__":
    print(Solution().minimum_window("cabwefgewcwaefgcf", "cae"))

