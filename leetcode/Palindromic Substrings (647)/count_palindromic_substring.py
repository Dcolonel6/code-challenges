class Solution:
    def count_substring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)
        s_standardized = f'#{"#".join(list(s))}#'
        previous_biggest_center = 0
        previous_biggest_right_boundary = 0
        length = len(s_standardized)
        radii = [0] * length
        number_of_palindromes = 0
        palindromes_ary = []
        left = 0
        right = 0

        for index in range(length):
            mirrored_index = 2 * previous_biggest_center - index

            if index < previous_biggest_right_boundary:
                radii[index] = min(radii[mirrored_index], previous_biggest_right_boundary - index)

            left = index - (radii[index] + 1)
            right = index + (radii[index] + 1)

            while left >= 0 and right < length and s_standardized[right] == s_standardized[left]:
                radii[index] += 1
                left -= 1
                right += 1

            if index + radii[index] > previous_biggest_right_boundary:
                previous_biggest_center = index
                previous_biggest_right_boundary = index + radii[index]

            number_of_palindromes += (radii[index] + 1) // 2

        return number_of_palindromes


if __name__ == "__main__":
    print(Solution().count_substring("aaa"))
