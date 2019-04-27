"""

a python script to find the longest common substring present in the dictionary of DNA strings
    rosalind LCSM
"""
from computing_gc_content import file_open


def find_shared_motif(file_path):
    fasta = file_open(file_path)
    print(fasta)
    first_strand = list(fasta.values())[0]
    print(first_strand)
    for key, value in fasta.items():
        # print(key)
        # print(value)
        x = len(first_strand)
        max_motif = first_strand[:x]
        print(f' this is {max_motif}')
        for i in fasta.values():
            print(fasta)
            for base in value:
                print(f' this is base {base}')


find_shared_motif('/Users/glen/Documents/find_shared_motif.txt')