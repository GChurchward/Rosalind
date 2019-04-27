"""

a script to give the reverse complementary strand of a DNA string
rosalind REVC
"""


def rev_comp(dna_string):
    """

    :param dna_string: a dna string
    :return: the reverse complementary dna string
    """
    string = dna_string
    string = string.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    print(string)
    return string


# rev_comp('ATGTTTA')