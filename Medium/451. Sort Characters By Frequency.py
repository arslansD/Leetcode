from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        my_str = ""
        s = Counter(s)
        new_list = sorted(zip(s.keys(), s.values()), key = lambda x:x[1], reverse = True)
        print(new_list)
        for my_tuple in new_list:
            my_str += my_tuple[0] * my_tuple[1]
        return  my_str

new = Solution()
print(new.frequencySort("aAbb"))
