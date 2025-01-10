from collections import Counter


class Solution:

    def check_inclusion(self, s1: str, s2: str) -> bool:
        counter_hash = Counter(s1)
        left = 0
        length = len(s1)

        for idx, letter in enumerate(s2):
            window = idx - left + 1
            if window == length:
                # check if window substr is a permtation of s1
                if counter_hash == Counter(s2[left: idx + 1]):
                    return True
                left += 1
        return False


if __name__ == "__main__":
    print(Solution().check_inclusion("ab", "eidbaooo"))
    print(Solution().check_inclusion("ab", "eidboaoo"))
