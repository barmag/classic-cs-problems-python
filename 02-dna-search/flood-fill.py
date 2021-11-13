from collections import deque
from typing import Counter, List
import unittest

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 4-directional [i, j]
        # [i-1, j], [i+1, j], [i, j-1], [i, j+1]
        frontier = deque()
        visited = set()
        frontier.append((sr, sc))
        val = image[sr][sc]
        image[sr][sc] = newColor
        while frontier:
            current = frontier.pop()
            if current not in visited:
                visited.add(current)
                # visit neighbors
                ne = [(current[0]-1, current[1]), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0], current[1]+1)]
                for n in ne:
                    o = False
                    for z in n:
                        if z < 0 or z > len(image)-1:
                            o = True
                    if not o and image[n[0]][n[1]] == val:
                        image[n[0]][n[1]] = newColor
                        frontier.append((n[0],n[1]))
                    # visited.add((sr, sc))
        return image



class TestCase(unittest.TestCase):
    def test_base(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        expected = [[2,2,2],[2,2,0],[2,0,1]]
        self.assertEqual(expected, Solution().floodFill(image, 1, 1, 2))


if __name__ == "__main__":
    unittest.main()