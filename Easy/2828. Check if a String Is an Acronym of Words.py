from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for index, element in enumerate(words):
            if element[0] != s[index]:
                return False
        return True

