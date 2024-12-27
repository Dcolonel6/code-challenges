from collections import Counter


class Anagram:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = Counter(s)
        t_counter = Counter(t)
        return s_counter == t_counter



if __name__ =="__main__":
    print(Anagram().is_anagram("anagram", "nagaram"))