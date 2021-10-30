import unittest

from enum import IntEnum
from typing import Coroutine, Tuple, List

Neuclotide: IntEnum = IntEnum('Neuclotide', ('A', 'C', 'G', 'T'))
Codon: Tuple = Tuple[Neuclotide, Neuclotide, Neuclotide]
Gene: List = List[Codon]

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

def string_to_gene(s: str) -> Gene:
    if len(s)%3 != 0:
        raise Exception('Gene length invalid')
    gene: Gene = []
    for i in range(0, len(s), 3):
        codon: Codon = (Neuclotide[s[i]], Neuclotide[s[i + 1]], Neuclotide[s[i + 2]])
        gene.append(codon)
    return gene

def binary_contains(gene: Gene, key: Codon) -> bool:
    low = 0
    high = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2

        if gene[mid] < key:
            low = mid + 1
        elif gene[mid] > key:
            high = mid - 1
        else:
            return True
    return False

class TestCase(unittest.TestCase):
    def test_valid_gene_length(self):
        with self.assertRaises(Exception):
            string_to_gene('ABCC')
    def test_valid_one_codon_gene(self):
        s = 'ACG'
        codon: Codon = (Neuclotide['A'], Neuclotide['C'], Neuclotide['G'])
        expected: Gene = []
        expected.append(codon)

        self.assertEqual(expected, string_to_gene(s))
    def test_find_at_front(self):
        key: Codon = (Neuclotide['A'], Neuclotide['C'], Neuclotide['G'])
        gene = sorted(string_to_gene(gene_str))
        found = binary_contains(gene, key)
        self.assertTrue(found)
    def test_find_at_back(self):
        key: Codon = (Neuclotide['T'], Neuclotide['T'], Neuclotide['T'])
        gene = sorted(string_to_gene(gene_str))
        found = binary_contains(gene, key)
        self.assertTrue(found)

    def test_find_at_mid(self):
        key: Codon = (Neuclotide['C'], Neuclotide['G'], Neuclotide['T'])
        gene = sorted(string_to_gene(gene_str))
        found = binary_contains(gene, key)
        self.assertTrue(found)
    
    def test_not_found(self):
        key: Codon = (Neuclotide['A'], Neuclotide['G'], Neuclotide['C'])
        gene = sorted(string_to_gene(gene_str))
        found = binary_contains(gene, key)
        self.assertFalse(found)
            
if __name__ == '__main__':
    unittest.main()
