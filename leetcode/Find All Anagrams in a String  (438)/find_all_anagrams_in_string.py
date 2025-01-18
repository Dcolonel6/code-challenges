from typing import List


class Solution:
    def find_anagrams(self, s: str, p: str) -> List[int]:
        count_of_p = [0] * 26
        count_of_sub_ary = [0] * 26
        length_of_p = len(p)
        left = 0
        answer = []
        # a list of all letters a-z then populate the frequency of each letter
        for i in p:
            # get difference between ord a and the i
            index = ord(i) - ord("a")
            # increase occurance count
            count_of_p[index] += 1

        # loop through s
        for index, letter in enumerate(s):
            window = index - left + 1
            i = ord(letter) - ord("a")
            count_of_sub_ary[i] += 1
            # check if window is same size as our potential anagram
            if window == length_of_p:
                left_letter = s[left]
                # check if subary is an anagram of p
                if count_of_sub_ary == count_of_p:
                    # subary is an anagram
                    answer.append(left)
                # decrease the count of left letter since we are shifting it to right by a step
                count_of_sub_ary[ord(left_letter) - ord("a")] -= 1
                left += 1
        return answer


if __name__ == "__main__":
    print(Solution().find_anagrams("cbaebabacd", "abc"))

