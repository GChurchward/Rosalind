"""

a script to return the adjacency list of a dna strings based on their overlap O
    rosalind GRPH
"""
import collections

from computing_gc_content import file_open


def overlap(file_path, overlap_len=3):
    fasta = file_open(file_path)
    for fasta_key in fasta:
        length = len(fasta[fasta_key])
        print(length)
    print(fasta)
    fasta = collections.OrderedDict(fasta)
    print(fasta)
    #for fasta_key, fasta_sequence in fasta.items():
    #    length = len(fasta_sequence)
    #    print(fasta_key, fasta_sequence)
    #    print(length)
    #  #  print(fasta_sequence[(length - overlap_len): length])
    #    overlap_end = fasta_sequence[(length - overlap_len): length]
    #    overlap_start = fasta_sequence[:overlap_len]
     #if overlap_end == overlap_start
    for  fasta_seq in fasta.items():
        #print(length, fasta_key, fasta_seq)
        #print(fasta_seq[1])
        for seq in fasta_seq:
            print(seq)
            if fasta_seq[(length - overlap_len): length] == fasta_seq[:overlap_len]:
                print(seq)
        #overlap_end = fasta_[(length - overlap_len): length]
        #overlap_start = fasta[index + 1][:overlap_len]
        #print(f'overlap_end = {overlap_end} and overlap_start = {overlap_start}')
        ##if fasta[fasta_key][overlap_end] == fasta[fasta_key][overlap_start]:


overlap('/Users/Glen/Documents/overlap_graph.txt')