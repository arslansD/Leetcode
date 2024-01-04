from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict1 = Counter(words1)
        dict2 = Counter(words2)
        final = 0

        for key, value in dict1.items():
            if key in dict2 and dict2.get(key) == value and value == 1:
                final += 1
        return final
