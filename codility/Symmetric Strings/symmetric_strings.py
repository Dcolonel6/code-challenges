class Solution:

    def solution(self, S):
        max_len = 0
        n = len(S)

        # Iterate through all possible even-length substrings
        for mid in range(n):
            left, right = mid, mid + 1
            left_count, right_count = 0, 0

            # Expand around the center as long as we can form a symmetric substring
            while left >= 0 and right < n:
                if S[left] == '<' or S[left] == '?':
                    left_count += 1
                if S[right] == '>' or S[right] == '?':
                    right_count += 1

                if left_count == right_count:
                    max_len = max(max_len, right - left + 1)

                left -= 1
                right += 1

        return max_len


if __name__ == "__main__":
    print(Solution().solution("??><??"))
