from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        final = 0
        for age in details:
            if int(age[-4:-2]) > 60:
                final += 1
        return final

example = Solution()
print(example.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
