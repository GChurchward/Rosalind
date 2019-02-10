#TODO split text via >
#TODO create dictionary using defined string length
#TODO link to the DNA string
#TODO calculate GC content of DNA string
#TODO equate value to dictionary
#TODO move through dictionary looking for highest and return highest string and GC content
import os


def string_split(s):
    data = open(os.path.expanduser(s), 'r')
    print(data)
    #list = data.split('>')
    #print(list)
    #li#st.pop(0)
    #print(list)

#string_split(">Rosalind_6404CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG>Rosalind_595CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATAATTTGTCAGCAGACACGC>Rosalind_0808CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT")

string_split('~/Downloads/test_case.txt')