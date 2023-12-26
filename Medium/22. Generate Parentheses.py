from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

s = Solution()
print(s.generateParenthesis(3))

        # Accidentally calculated Catalan's number. Will keep it here
        # fact = 1
        # fact2 = 1
        # fact3 = 1
        # for element in range(1, 2 * n + 1):
        #     fact *= element
        #     if element == n+1:
        #         fact2 = fact
        #     if element == n:
        #         fact3 = fact
        #
        #
        # return int(fact / (fact2 * fact3))
        #(2n)! / ((n + 1)! * n!)

