"""

Script to determine amino acid sequence from RNA strand
    rosalind PROT
"""


# TODO check  string as elements 0,1,2 until aug is found and use those deleting the elements before that
# TODO cycle through the whole chain checking for multiple sequences


def rna_to_protein(rna_sequence):
    """
    :param rna_sequence: sequence of RNA
    :return: Amino acids correlating to codons in RNA string
    """
    codon = []
    if (len(rna_sequence) % 3) >= 1:
        raise ValueError

    for letter in rna_sequence:
        # if letter != 'G' or 'A' or 'C' or 'U':
        if letter not in ['G', 'A', 'C', 'U']:
            raise ValueError

    length = int((len(rna_sequence) / 3))
    print(rna_sequence)
    print(length)
    amino_acid_chain = []
    protein = ''

    codon_map = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
                 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
                 'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 'UAG': 'STOP',
                 'UGU': 'C', 'UGC': 'C', 'UGA': 'STOP', 'UGG': 'W',
                 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
                 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
                 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                 'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
                 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
                 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
                 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

    for i in range(0, length):
        codon.append(rna_sequence[(3 * i):((3 * i) + 3)])
    print(codon)
    # print(codon_map)

    for element in codon:
        amino_acid_chain.append(codon_map[element])

    print(amino_acid_chain)

    for i in amino_acid_chain:
        if i == 'STOP':
            break
        else:
            protein += i
    print(protein)
    return protein

# check works
# rna_to_protein('ACUGCUGACCAU')

# check stop codon works
# rna_to_protein('AUGCGUCUUUAG')

# check for length of string
# rna_to_protein('AUCCG')

# check for incorrect base
# rna_to_protein('ACTGTUAUG')

# assert (rna_to_protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA') == 'MAMAPRTEINSTRING')

# rna_to_protein('')
