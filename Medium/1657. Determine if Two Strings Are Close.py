from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        char1 = Counter(word1)
        char2 = Counter(word2)
        if (char1.keys() == char2.keys()
                and sorted(char1.values()) == sorted(char2.values())): # если все числа по порядку, то подходит
                return True
        return False
