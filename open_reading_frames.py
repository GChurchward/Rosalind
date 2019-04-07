"""

a script to return any candidate protein strings that can be formed from the respective dna string
    rosalind ORF
"""
from complementary_strand import rev_comp
from computing_gc_content import file_open
from dna_to_rna import dna_to_rna


def reading_frames(file_path):
    """

    :param file_path: takes file path location
    :return: dictionary of dna strand and complementary dna strand
    """
    fasta = file_open(file_path)
    # print(fasta)
    fasta_with_comp = {}
    for fasta_key, fasta_value in fasta.items():
        fasta_with_comp[fasta_key] = fasta_value
        new_key = str(fasta_key) + '_1'
        # print(new_key)
        fasta_with_comp[new_key] = rev_comp(fasta_value)
    print(fasta_with_comp)
    return fasta_with_comp


def rna_strings_from_dict(file_path):
    """

    :param file_path: file location
    :return: a list of rna strings
    """

    fasta_with_comp = reading_frames(file_path)
    start_positions = []
    rna_strings = []
    for fasta_key, fasta_value in fasta_with_comp.items():
        rna_sequence = dna_to_rna(fasta_value)
        # print(fasta_value)
        fasta_with_comp[fasta_key] = rna_sequence
        print(fasta_with_comp)
    for fasta_value in fasta_with_comp.values():
        print(fasta_value)
        for index, base in enumerate(fasta_value):
            # print(index)
            # print(base)
            print(fasta_value[index: (index+3)])
            if fasta_value[index: (index+3)] == 'AUG':
                print(index)
                rna_strings.append(fasta_value[index: len(fasta_value)])
                start_positions.append(index)
        print(rna_strings)
        print(start_positions)
    return rna_strings


def rna_to_codon(rna_sequence):
    """
    :param rna_sequence: sequence of RNA
    :return: a list of codons for respective rna
    """
    codon = []
    if (len(rna_sequence) % 3) >= 1:
        raise ValueError

    for letter in rna_sequence:
        # if letter != 'G' or 'A' or 'C' or 'U':
        if letter not in ['G', 'A', 'C', 'U']:
            raise ValueError

    length = int((len(rna_sequence) / 3))
    # print(rna_sequence)
    # print(length)

    for i in range(0, length):
        codon.append(rna_sequence[(3 * i):((3 * i) + 3)])
    # print(codon)
    # print(codon_map)
    return codon


def codon_to_protein(rna_sequence):
    """

    :param rna_sequence: an rna sequence
    :return: an amino acid chain but returning not in if does not contain a stop codon
    """
    codon = rna_to_codon(rna_sequence)
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
    for element in codon:
        amino_acid_chain.append(codon_map[element])

    # print(amino_acid_chain)
    if 'STOP' not in amino_acid_chain:
        print('not in')
        return

    for i in amino_acid_chain:
        if i == 'STOP':
            break
        else:
            protein += i
    # print(protein)
    return protein


def candidate_protein(file_path):
    """

    :param file_path: file path location
    :return: all possible candidate proteins that can be made from a dna string
    """
    rna_strings = rna_strings_from_dict(file_path)
    corrected_rna = []
    total_protein_list = []
    for sequence in rna_strings:
        # print(rna_strings)
        seq_len = len(sequence)
        # print(seq_len)
        new_len = int(seq_len / 3)
        # print(new_len)
        # print(sequence)
        corrected_rna.append(sequence[0: new_len*3])
        # print(corrected_rna)
    for rna_sequence in corrected_rna:
        protein = codon_to_protein(rna_sequence)
        if protein is None:
            pass
        else:
            total_protein_list.append(protein)
            print(protein)
    # print(total_protein_list)
    protein_list = []
    for i in total_protein_list:
        if i not in protein_list:
            protein_list.append(i)
    print(protein_list)
    for item in protein_list:
        print(item)
    return protein_list


# rna_to_codon('UUAAGGCCCUAG')
# codon_to_protein(['UUA', 'AGG', 'CCC'])
candidate_protein('/Users/Glen/Downloads/rosalind_orf.txt')
