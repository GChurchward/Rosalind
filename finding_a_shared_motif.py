"""

a python script to find the longest common substring present in the dictionary of DNA strings
    rosalind LCSM
"""
from copy import copy
from time import time
from computing_gc_content import file_open


#def detect_motif(motif, remain_sequences):



def find_shared_motif(file_path):
    fasta_dict = file_open(file_path)
    print(fasta_dict)
    fasta = fasta_dict.values()
    print(fasta)
    fasta = list(fasta)
    #fasta = sorted(fasta, key=len)
    print(fasta)
    shortest = fasta[0]
    print(shortest)
    possible_motifs = find_possible_motifs(shortest)
    print(possible_motifs)
    for remain_sequences in fasta[1:]:
        for motif in copy(possible_motifs):
            if not motif in remain_sequences:
                print('{} not in {}'.format(motif, remain_sequences))
                possible_motifs.remove(motif)
    sorted_motifs = sorted(possible_motifs, key=len)
    longest_motif = sorted_motifs[-1]
    print(longest_motif)
    return longest_motif

def find_possible_motifs(sequence):
    possible_motifs = set()
    for start in range(0, len(sequence)+1):
        for end in range(start+1, len(sequence)+1):
            possible_motifs.add(sequence[start:end])
    return possible_motifs

now = time()
find_shared_motif('/Users/glen/Downloads/rosalind_lcsm.txt')
then = time()
print(then - now)