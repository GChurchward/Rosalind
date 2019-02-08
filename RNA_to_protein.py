#TODO take string and split into sets of 3 letters
#TODO take list of codons create if statements for RNA codons
#TODO append letters of codons to a list
#TODO turn list to string



def rna_to_protein(s):
    """
    :param s:
    :return:
    """
    codon = []
    if (len(s) % 3) >= 1:
        raise ValueError

    for letter in s:
        # if letter != 'G' or 'A' or 'C' or 'U': #TODO fix this checking for incorrect base
        if letter not in ['G', 'A', 'C', 'U']:
            raise ValueError

    length = int((len(s) / 3) + 1)
    print(s)
    print(length)
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

    for i in range(1, length):
        codon.append(s[((3 * i) - 3):((3 * i))])
    print(codon)
    #print(codon_map)

    for element in codon:
        amino_acid_chain.append(codon_map[(element)])

    print(amino_acid_chain)

    for i in amino_acid_chain:
        if i == 'STOP':
            break
        else:
            protein += i

    print (protein)

#check works
rna_to_protein('ACUGCUGACCAU')

#check stop codon works
#rna_to_protein('AUGCGUCUUUAG')

#check for length of string
#rna_to_protein('AUCCG')

#check for incorrect base
#rna_to_protein('ACTGTUAUG')