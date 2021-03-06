"""

a script to return the gc content of a collection of dna string in a txt fasta format file
    rosalind GC
"""
#TODO move through dictionary looking for highest and return highest string and GC content


def file_open(file_path):
    """
    taking a fasta fle format and returning a dictionary of the sequence id and sequence
    :param file_path: path to file
    :return: dictionary where key is sequence id and value is the sequence
    """
    fasta = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                sequence_id = line[1:]
                # print(line)
                # print(sequence_id)
                if sequence_id not in fasta:
                    fasta[sequence_id] = ''
                    #print(f'**** adding new key {sequence_id}', fasta)
            if not line.startswith('>'):
                sequence = line
                #print(sequence)
                fasta[sequence_id] += sequence
                #print(fasta)
    return fasta


def gc_compute(filepath):
    """

    :param filepath: path to file of fsata format dna strings
    :return: gc content of the dna sequences
    """
    fasta = file_open(filepath)
    print(f' fasta is {fasta}')
    for fasta_key, fasta_value in fasta.items():
        length = len(fasta[fasta_key])
        # print(length)
        highest_content = 0
        # print(highest_content)
        gc_count = 0
        # print(gc_count)
        for base in fasta_value:
            if base == 'C' or base == 'G':
                gc_count += 1
                gc_percentage = (gc_count / length) * 100
                #print(gc_count)
                #print(gc_percentage)
        if gc_percentage > highest_content:
            highest_content = gc_percentage
            print(fasta_key)
            print(f'highest content = {highest_content}')
    return fasta_key, highest_content



