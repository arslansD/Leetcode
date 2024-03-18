from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(len(s) if any(c.isalpha() for c in s) else int(s)
                   for s in strs)


example = Solution()
print(example.maximumValue(["1","01","001","0001"]))
