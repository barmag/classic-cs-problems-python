import unittest
from unittest import result

def qsort(tosort):
    if len(tosort) < 2:
        return tosort
    if len(tosort) == 2:
        if tosort[1] < tosort[0]:
            return [tosort[1], tosort[0]]
        return [tosort[0], tosort[1]]
    pivot = tosort[0]
    left = [k for k in tosort[1:] if k < pivot]
    right = [k for k in tosort[1:] if k >= pivot]
    result = qsort(left) + [pivot] + qsort(right )
    return result

class QSort_Test(unittest.TestCase):
    def test_base_case(self):
        tosort = [1]
        t2 = []
        result = qsort(tosort)
        self.assertEqual(result, tosort)
        self.assertEqual(t2, qsort(t2))
    
    def test_len_2(self):
        t1 = [1, 2]
        t2 = [2, 1]
        self.assertEqual(t1, qsort(t1))
        self.assertEqual(t1, qsort(t2))

    def test_gen_case(self):
        t1 = [6, 5, 2, 9, 4, 5, 8, 7, 1, 3]
        t2 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
        self.assertEqual(t2, qsort(t1))

if __name__ == '__main__':
    unittest.main()