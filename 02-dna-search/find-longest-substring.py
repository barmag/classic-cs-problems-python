import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        i = 0
        while i < len(s) - n:
            current = {s[i]}
            n = max(1, n)
            j = i + 1
            while  j <= len(s) - 1 and s[j] not in current:
                current.add(s[j])
                n = n+1 if j-i+1>n else n
                j += 1
            i += 1
        return n

class Test(unittest.TestCase):
    def t8est_base(self):
        s = "abcabcbb"
        expected = 3
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)
    
    def test_base2(self):
        s = "au"
        expected = 2
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)

if __name__ == '__main__':
    unittest.main()