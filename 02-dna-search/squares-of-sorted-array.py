import unittest
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # naive implementation
        # squares = [n ** 2 for n in nums]
        # return sorted(squares)
        squares = [0] * len(nums)
        left, right = 0, len(nums)-1
        while(left <= right):
            l, r = abs(nums[left]), abs(nums[right])
            if l > r:
                squares[right - left] = l**2
                left += 1
            else:
                squares[right-left] = r**2
                right -= 1
        return squares
class SolutionTest(unittest.TestCase):
    def testBasic(self):
        n = [-4,-1,0,3,10]
        expected = [0,1,9,16,100]
        actual = Solution().sortedSquares(n)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()