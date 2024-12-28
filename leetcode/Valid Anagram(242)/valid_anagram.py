from collections import Counter


class Anagram:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # s_counter = Counter(s)
        # t_counter = Counter(t)
        # return s_counter == t_counter
        return self.is_anagram_with_prime(s) == self.is_anagram_with_prime(t)

    def is_anagram_with_prime(self, word: str) -> bool:
        # Prime mapping for each lowercase letter (a-z)
        primes = {
            'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11,
            'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
            'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47,
            'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
            'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101
        }
        product = 1
        for char in word:
            product *= primes[char]
        return product


if __name__ =="__main__":
    print(Anagram().is_anagram("anagram", "nagaram"))