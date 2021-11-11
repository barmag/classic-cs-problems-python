# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # brute force
        # for i in range(0, n+1):
        #     if(isBadVersion(i)):
        #         return i
        
        # naive binary
        low, high = 0, n
        
        while low <= high:
            mid = (low + high) // 2
            
            isBad = isBadVersion(mid)
            prevBad = isBadVersion(mid-1)
            nextBad = isBadVersion(mid-1)
            if isBad and not prevBad:
                return mid
            if prevBad:
                high = mid - 1
            else:
                low = mid + 1
        