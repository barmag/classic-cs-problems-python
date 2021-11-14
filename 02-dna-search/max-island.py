import unittest
from typing import List
import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        current_island = set()
        max_len = 0
        
        frontier = []
        frontier.append((0, 0))
        visited = {(0, 0)}
        explored_land = set()

        while frontier:
            current = frontier.pop()
            visited.add(current)
            neighbors = [(current[0]-1, current[1]), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0], current[1]+1)]

            if grid[current[0]][current[1]] == 1:
                land_f = collections.deque()
                land_f.append(current)
                current_island = {current}
                while land_f:
                    c_land = land_f.popleft()
                    n_land = [(c_land[0]-1, c_land[1]), (c_land[0]+1, c_land[1]), (c_land[0], c_land[1]-1), (c_land[0], c_land[1]+1)]
                    found_land = False
                    for next_n in n_land:
                        if next_n[0] >= 0  and next_n[0] < len(grid) and next_n[1] >= 0 and next_n[1] < len(grid[0]) and grid[next_n[0]][next_n[1]] == 1 and next_n not in current_island:
                            land_f.append(next_n)
                            found_land = True
                            current_island.add(next_n)
                    if not found_land:
                        break
                max_len = max(max_len, len(current_island))

            for next_n in neighbors:
                if next_n[0] >= 0  and next_n[0] < len(grid) and next_n[1] >= 0 and next_n[1] < len(grid[0]) and next_n not in visited:
                    visited.add(next_n)
                    frontier.append(next_n)
            # if not found_land:
            #     max_len = max(max_len, len(current_island))
            #     current_island.clear()

        return max_len
        

class TestCase(unittest.TestCase):
    def test_traverse(self):
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        self.assertEqual(6, Solution().maxAreaOfIsland(grid))

if __name__ == "__main__":
    unittest.main()