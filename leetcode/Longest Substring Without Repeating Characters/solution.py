class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        tracker = {}
        left = 0

        for index, letter in enumerate(s):

            while letter in tracker:
                left_letter = s[left]
                tracker.pop(left_letter)
                left += 1
            tracker[letter] = index
            window = index - left + 1
            max_length = max(max_length, window)
        return max_length

    def length_of_longest_substring_diff_approach(self, s: str) -> int:
        max_length = 0
        tracker = {}
        left = 0
        index = 0
        length = len(s)
        substr = []

        while index < length:
            letter = s[index]
            if letter in tracker:
                # if it exist, then we have encountered a duplicate, move left pointer
                if tracker[letter] >= left:
                    left = tracker[letter] + 1
            tracker[letter] = index
            substr.append(s[left: index+1])
            # always compares our previous window with the currrent one, returns the largest
            max_length = max(max_length, (index - left) + 1)
            index += 1
        print(substr)
        return max_length


if __name__ == "__main__":
    print(Solution().length_of_longest_substring_diff_approach("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("abcabcbb"))



