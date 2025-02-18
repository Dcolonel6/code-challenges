class Solution:

    def length_palindrome(self, s: str) -> (str, int):
        if len(s) <= 1:
            return s

        string = "#".join(list(s))
        string = f"#{string}#"
        length = len(string)
        max_length = 0
        largest_palindrome = ""
        radii = [0] * length
        previous_center = 0
        previous_right_boundary = 0

        for index in range(length):
            # find mirrored index
            mirrored_index = 2 * previous_center - index
            # check if the current index is within the furthest right of the previous center
            if index < previous_right_boundary:
                # use the mirrored index to get the radius of that mirrored index
                radii[index] = min(radii[mirrored_index], index - previous_right_boundary)
            # expansion
                # expand if left letter == right letter and left >= 0 and right less than length
            left = index - (radii[index] + 1)
            right = index + (radii[index] + 1)
            while left >= 0 and right < length and string[left] == string[right]:
                # increase radius
                radii[index] += 1
                # increase right by one
                right += 1
                # decrease left by one
                left -= 1
            # check if our largest palindrome right boundary has exceeded the previous palindrome right boundary
            if index + radii[index] > previous_right_boundary:
                # if it has, update previous center to be current index and previous_right_boundary to
                # be current right boundary
                previous_center = index
                previous_right_boundary = index + radii[index]
            # extract the palindrome
            current_palindrome = string[left+1: right].replace("#", "")
            current_len_palindrome = len(current_palindrome)

            if max_length < current_len_palindrome:
                max_length = current_len_palindrome
                largest_palindrome = current_palindrome

        return largest_palindrome


if __name__ == "__main__":
    # print(Solution().length_palindrome("babad")) # "bab"
    print(Solution().length_palindrome("abaxabaxabb")) # "noon"



