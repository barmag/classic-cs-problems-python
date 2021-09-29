"""
A class to store a Gene string in a compressed form
"""

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.bit_string = 1
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        for nuclotide in gene.upper():
            self.bit_string <<= 2
            if nuclotide == "A":
                self.bit_string |= 0b00
            elif nuclotide == "C":
                self.bit_string |= 0b01
            elif nuclotide == "G":
                self.bit_string |= 0b10
            elif nuclotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalied nuclotide {nuclotide}")
        
    def decompress(self) -> str:
        # print(self.bit_string)
        # print(self.bit_string.bit_length())
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            # print(bits)
            if bits == 0b00:
                gene += "A"
                # print("found A")
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid bits {bits}")
        # print(gene)
        return gene[::-1]
    def __str__(self) -> str:
        return self.decompress()

if __name__ == "__main__":
    original: str = "TAGGGCATCCCATT"
    compressed: CompressedGene = CompressedGene(original)
    decopmpressed = compressed.decompress()
    print(decopmpressed)
    print(f"decompressed {original == decopmpressed}")