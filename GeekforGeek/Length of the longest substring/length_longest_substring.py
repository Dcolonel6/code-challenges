
class Solution:
    def longest_unique_substring(self, s: str) -> int:
        left = 0
        max_length = float("-inf")
        tracker = {}

        for index, letter in enumerate(s):
            # check if letter is in tracker
            while letter in tracker and left <= index:
                # yes, we have a duplicate letter
                # move the left pointer
                left_letter = s[left]
                tracker.pop(left_letter)
                left += 1
            window = index - left + 1
            max_length = max(max_length, window)
            tracker[letter] = index

        return max_length if max_length != float("inf") else 0


if __name__ == "__main__":
    print(Solution().longest_unique_substring("aaaaa"))
