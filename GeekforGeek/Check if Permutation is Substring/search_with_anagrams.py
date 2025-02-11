
class Solution:
    def search(self, text: str, pat: str) -> bool:
        pat_map = [0] * 26
        left = 0
        window_map = [0] * 26
        length = len(pat)

        for letter in pat:
            i = ord(letter) - ord("a")
            pat_map[i] += 1

        for idx, char in enumerate(text):
            window = idx - left + 1
            index = ord(char) - ord("a")
            window_map[index] += 1

            if length == window:
                left_char = text[left]
                index_left_char = ord(left_char) - ord("a")
                # is the window the same as pat
                if window_map == pat_map:
                    return True
                window_map[index_left_char] -= 1
                left += 1
        return False


if __name__ == "__main__":
    print(Solution().search("programming",  "rain"))
