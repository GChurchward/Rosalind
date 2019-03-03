"""

script to return the consensus of a selection of dna strings
    rosalind CONS
"""
from computing_gc_content import file_open


def base_counting(file_path):
    """

    :param file_path: path to file location
    :return:list of dictionaries with counts of bases
    """
    fasta = file_open(file_path)
    # print(fasta)
    sequences = []

    # print(sequences)

    counts = []
    for fasta_key in fasta:
        sequences.append(fasta[fasta_key])
    # print(sequences)
    length = sequences[0]
    for i in length:
        counts.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
    # print(counts)
    # print(len(counts))
    for sequence in sequences:
        # print(sequences)
        # print(sequence)
        for idx, base in enumerate(sequence):
            # print(counts[int(idx)])
            counts[idx][base] += 1
    # print(counts)
    return counts


def consensus(file_path):
    """

    :param file_path: takes file path of fasta format files
    :return: consensus dna string
    """
    counts = base_counting(file_path)
    consensus_sequence_list = []
    consensus_sequence = ''
    for position in counts:
        # print(position)
        most_common_base = ''
        count = 0
        for base in position:
            # print(base)
            if position[base] > count:
                count = position[base]
                most_common_base = base
                # print(f' most common base is {most_common_base} with a count of {count}')
        consensus_sequence_list.append(most_common_base)
    # print(consensus_sequence_list)
    for base in consensus_sequence_list:
        consensus_sequence += base
    print(consensus_sequence)
    return consensus_sequence


def base_matrix(file_path):
    """

    :param file_path: takes file path of fasta format files
    :return: matrix of bases at each position
    """
    counts = base_counting(file_path)
    a_counts = ''
    c_counts = ''
    g_counts = ''
    t_counts = ''
    for position in counts:
        # print(position)
        for base in position:
            # print(base)
            value = str(position[base])
            # print(value)
            if base == 'A':
                a_counts += value
                # print(a_counts)
            if base == 'C':
                c_counts += value
                # print(c_counts)
            if base == 'G':
                g_counts += value
                # print(g_counts)
            if base == 'T':
                t_counts += value
                # print(t_counts)
    a_counts = ' '.join(a_counts)
    print('A: ' + a_counts)
    c_counts = ' '.join(c_counts)
    print('C: ' + c_counts)
    g_counts = ' '.join(g_counts)
    print('G: ' + g_counts)
    t_counts = ' '.join(t_counts)
    print('T: ' + t_counts)
    return a_counts, c_counts, g_counts, t_counts


def consensus_return(filepath):
    consensus(filepath)
    base_matrix(filepath)
    return


consensus_return('/Users/Glen/Downloads/rosalind_cons.txt')