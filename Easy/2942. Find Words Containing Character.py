from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        final = []
        for index, element in enumerate(words):
            if x in element:
                final.append(index)
        return final
