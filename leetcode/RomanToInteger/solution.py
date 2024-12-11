class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
#iv
        length = len(s)
        current = 0
        number = 0

        while current < length:
            current_letter = s[current]
            if current + 1 < length:
                next_letter = s[current + 1]
                if mappings[current_letter] >= mappings[next_letter]:
                    # normal ordering so we add
                    number += mappings[current_letter]
                    current += 1
                else:
                    result = mappings[next_letter] - mappings[current_letter]
                    number += result
                    current += 2
            else:
                number += mappings[current_letter]
                current += 1
        return number


if __name__ == "__main__":
    print(Solution().romanToInt(("III")))
    print(Solution().romanToInt(("IV")))
    # print(Solution().romanToInt(("LVIII")))
    # print(Solution().romanToInt(("MCMXCIV")))
