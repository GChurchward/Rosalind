#TODO split text via >
#TODO create dictionary using defined string length
#TODO link to the DNA string
#TODO calculate GC content of DNA string
#TODO equate value to dictionary
#TODO move through dictionary looking for highest and return highest string and GC content
from itertools import islice


def file_open(file_path):
    vari = []
    fasta = []
    with open(file_path, 'r') as f:
        g = f.read()
        for line in g:
            line = line.strip()
            vari.append(line)

    chevron = [i for i, x in enumerate(vari) if x == ">" or x == "\n"]
    print(chevron)
    print(vari)

file_open('/Users/Glen/PycharmProjects/Rosalind/test_case.txt')