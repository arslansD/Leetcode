class Solution:
    def finalString(self, s: str) -> str:
        final = []
        for element in s:
            if element == "i":
                final.reverse()
            else:
                final.append(element)
        return "".join(final)

