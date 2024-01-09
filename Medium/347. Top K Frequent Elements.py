from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter(nums)
        frequency = dict(sorted(my_dict.items(), key = lambda x: x[1], reverse = True))

        result = list(frequency.keys())[:k]

        return result
