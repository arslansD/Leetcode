from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        final = 0
        for word in words[left:right+1]:
            if word[0] in 'aeiou' and word[-1]  in 'aeiou':
                final += 1
        return final

example = Solution()
print(example.vowelStrings(["are","amy","u"], 0, 2))
