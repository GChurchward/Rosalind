"""

a script to return the protein string based on removing introns from the dna sequence, converting the sequence to rna
and then returning the protein string
    rosalind SPLC
"""
from RNA_to_protein import rna_to_protein
from computing_gc_content import file_open


def rna_splicing(filepath):
    """

    :param filepath:path to fasta file txt
    :return: returns dna sequence with introns removed
    """
    fasta = file_open(filepath)
    print(fasta)
    longest = 0
    sequence = ''
    introns = []
    for fasta_key in fasta:
        if len(fasta[fasta_key]) > longest:
            longest = len(fasta[fasta_key])
            sequence = fasta[fasta_key]
            # print(f' sequence is: {sequence} and longest is {longest}')
        else:
            introns.append(fasta[fasta_key])
            # print(introns)

    for i in introns:
        # print(sequence)
        if i in sequence:
            sequence = sequence.replace(i, '')
            # print(sequence)
            # print(f' new sequence length is {len(sequence)} and length of intron is {len(i)}')
    return sequence


def dna_to_rna(sequence):
    """

    :param sequence: dna sequence as a string
    :return: rna sequence as a string
    """
    for i in sequence:
        if i == "T":
            sequence = sequence.replace('T', 'U')
            # print(sequence)
    return sequence


def intron_neg_dna_to_protein(filepath):
    fasta = rna_splicing(filepath)
    # print(fasta)
    sequence = dna_to_rna(fasta)
    # print(sequence)
    protein = rna_to_protein(sequence)
    # print(protein)
    return protein

# print(intron_neg_dna_to_protein('/Users/Glen/Documents/rna_splicing.txt') == 'MVYIADKQHVASREAYGHMFKVCA')

intron_neg_dna_to_protein('/Users/Glen/Downloads/rostxt')