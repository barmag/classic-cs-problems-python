import unittest

from enum import IntEnum
from typing import Tuple, List

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
            
if __name__ == '__main__':
    unittest.main()
