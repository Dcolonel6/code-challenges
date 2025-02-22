class Solution:
    def longest_symmetric_substring(self, s: str) -> int:
        n = len(s)
        max_length = 0

        # Iterate over all possible even-length substrings
        for mid in range(1, n):
            left, right = mid - 1, mid
            left_count, right_count = 0, 0

            while left >= 0 and right < n:
                if s[left] in {'<', '?'}:
                    left_count += 1
                else:
                    break

                if s[right] in {'>', '?'}:
                    right_count += 1
                else:
                    break

                if left_count == right_count:
                    max_length = max(max_length, right - left + 1)

                left -= 1
                right += 1

        return max_length


if __name__ == "__main__":
    print(Solution().longest_symmetric_substring("??><??"))
