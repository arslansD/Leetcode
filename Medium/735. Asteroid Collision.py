from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        final = []
        for element in asteroids:
            while final and final[-1] > 0 and element < 0:
                if final[-1] + element < 0: final.pop()
                elif final[-1] + element > 0: break
                elif final[-1] + element == 0: final.pop(); break
            else:
                final.append(element)
        return final

