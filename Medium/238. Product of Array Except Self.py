from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numslen = len(nums)
        ans = [1] * numslen

        for i in range(1, numslen):
            ans[i] = ans[i - 1] * nums[i - 1]

        suffix = 1
        for i in range(numslen - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
