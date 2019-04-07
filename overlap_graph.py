"""

a script to return the adjacency list of a dna strings based on their overlap O
    rosalind GRPH
"""

from computing_gc_content import file_open


def overlap(file_path, overlap_len=3):
    fasta = file_open(file_path)
    for fasta_key, current_seq in fasta.items():
        # current_seq = fasta[fasta_key]
        for k, v in fasta.items():
            last_three = current_seq[-overlap_len:]
            # print(last_three)
            if k != fasta_key:
                # print (k)
                # print (v[:3])
                if last_three == v[:overlap_len]:
                    print(fasta_key, k)
    return



overlap('/Users/Glen/Downloads/rosalind')