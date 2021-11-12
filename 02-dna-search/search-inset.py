import unittest
from typing import List
from unittest import result

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # first do just the search
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            # prev, nxt = nums[max(0,mid-1)], nums[min(mid+1, len(nums)-1)]
            # if mid == 0 and target < guess:
            #     return mid
            # if mid == len(nums)-1 and target > guess:
            #     return mid + 1
            # if target > prev and target < nxt:
            #     return mid
            
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
        return low


class SolutionTest(unittest.TestCase):
    def ttest_basicSearch(self):
        nums = [3, 5, 7, 8, 10]
        target, loc = 8, 3
        sol = Solution()
        result = sol.searchInsert(nums, target)
        self.assertEqual(result, loc)
    
    def ttest_insert1(self):
        nums = [1,3,5,6]
        target, loc = 2, 1
        result = Solution().searchInsert(nums, target)
        self.assertEqual(result, loc)
    
    def test_insert1(self):
        nums = [1,3]
        target, loc = 2, 1
        result = Solution().searchInsert(nums, target)
        self.assertEqual(result, loc)

if __name__ == "__main__":
    unittest.main()