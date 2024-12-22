class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        tracker = {}
        left = 0
        index = 0
        max_length = 0
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
    print(Solution().lengthOfLongestSubstring("abcabcbb"))

