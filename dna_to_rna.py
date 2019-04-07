"""

a script to convert a DNA string to RNA
rosalind RNA
"""


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

