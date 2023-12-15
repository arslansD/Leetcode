from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0  # for counting left window
        for j in range(len(nums)):  # for counting right window
            k -= 1 - nums[j]  # each move we do -1 if we meet 0. If not, nothing happens
            if k < 0:  # if we expire all 0, then we move left window
                k += 1 - nums[i]  # before we move, we add count to K, if the number was 0
                i += 1  # moving left windows
        return j - i + 1  # len(nums) - smallest i + 1 pos is our answer
