"""

a script to return any candidate protein strings that can be formed from the respective dna string
    rosalind ORF
"""
from computing_gc_content import file_open
from dna_to_rna import dna_to_rna


def reading_frames(file_path):
    """

    :param file_path: takes file path location
    :return: list of possible proteins from the dna sequence
    """
    fasta = file_open(file_path)
    print(fasta)
    start_positions = []
    rna_strings = []
    for fasta_key, fasta_value in fasta.items():
        rna_sequence = dna_to_rna(fasta_value)
        print(rna_sequence)
        fasta[fasta_key] = rna_sequence
        print(fasta)
        for base in range(0, len(rna_sequence)):
            # print(i)
            # print(rna_sequence[i: (i+3)])
            if rna_sequence[base: (base+3)] == 'AUG':
                # print(i)
                rna_strings.append(rna_sequence[base: len(rna_sequence)])
                start_positions.append(base)
        # print(start_positions)
        # print(rna_strings)
    for sequence in rna_strings:
        print(sequence)




reading_frames('/Users/Glen/Documents/open_reading_frames.txt')
