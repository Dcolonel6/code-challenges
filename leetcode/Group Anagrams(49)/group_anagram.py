from collections import Counter
from typing import List


class GroupAnagram:

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        for index, word in enumerate(strs):
            product_prime = self.alphabet_mapped(word)
            if product_prime in tracker:
                tracker[product_prime] = tracker[product_prime] + [word]
            else:
                tracker[product_prime] = [word]
        return list(tracker.values())

    def anagram_prime_fctors(self, str1: str) -> int:
        primes = {
            'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11,
            'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
            'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47,
            'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
            'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101
        }
        product = 1
        for letter in str1:
            product *= primes[letter]
        return product

    def alphabet_mapped(self, word):
        alphabet_ary = [0] * 26

        for letter in word:
            index = ord(letter) - ord("a")
            alphabet_ary[index] += 1

        return tuple(alphabet_ary)



if __name__ == "__main__":
    print(GroupAnagram().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
