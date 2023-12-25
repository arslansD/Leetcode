import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort_func(a, b):
            aa = str(a)
            bb = str(b)
            return aa + bb > bb + aa and 1 or -1

        return "".join(map(str, sorted(nums, key=functools.cmp_to_key(sort_func), reverse=True))).lstrip("0") or "0"
s = Solution()
print(s.largestNumber([0,0,0]))
