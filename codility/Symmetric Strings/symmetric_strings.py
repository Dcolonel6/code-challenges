class Solution:
    def longest_symmetric_substring(self, s: str) -> int:
        n = len(s)

        n = len(s)
        max_length = 0

        # Try each possible midpoint (between characters)
        for mid in range(n + 1):
            # For each midpoint, extend to both sides checking validity
            # Maximum possible left length from this midpoint
            left_count = 0
            for i in range(mid - 1, -1, -1):
                if s[i] == '<' or s[i] == '?':
                    left_count += 1
                else:
                    break

            # Maximum possible right length from this midpoint
            right_count = 0
            for i in range(mid, n):
                if s[i] == '>' or s[i] == '?':
                    right_count += 1
                else:
                    break

            # The symmetric substring length is limited by the minimum of left and right counts
            current_length = 2 * min(left_count, right_count)
            max_length = max(max_length, current_length)

        return max_length


if __name__ == "__main__":
    print(Solution().longest_symmetric_substring("??><??"))
