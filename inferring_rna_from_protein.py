"""

script to return the number of remainders based on modulo 1000000 of the possible number of rna sequences based on
the protein string

"""
codon_to_rna = {'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6,
                'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2}


def protein_to_rna(protein_string):
    """

    :param protein_string: A string of protein amino acids
    :return: number of possibilities of rna strand
    """
    protein_list = []
    possibilities = 1
    for i in protein_string:
        protein_list.append(i)
    for i in protein_list:
        possibilities = possibilities * codon_to_rna[i]
    print(f'number of poss without stop codon {possibilities}')
    possibilities = (possibilities * 3) % 1000000
    print(f' poss modulo 1000000: {possibilities}')
    return possibilities


protein_to_rna('MATTTY')

protein_to_rna('MACKPQFFMCSQVEDWMRAVFAPDDSMLHPPAYERVYKAATEGPKRSQSYEWWDDGGYWMEPHINENQDDMSQNDIEPAAYDSRSDASLCFTGWMQRSAAESMCNIEEPSEKRYINDAKNAYMEGHPKNHAADHVWYCEWYRFCEKPDTWAKNDYKFCQRQRHWDALFCMEAPGKTHFWEMIISSYYVIIRLSCDTFWVLKGYEGIAAEKQITNNTPVIEKGIEMGSGQFHGYFMVANAAGPDTRKNSRVPGKMHDKADDDPSIIFLCPHLFRGDIPCERQLCTCWPQLIHFKGQWIMAMFPAWEYNWPPQRKDHGAGITFCVVVWVWNPKMYKPGMMWCEELEMVNMFPYTIFNRWLAANGGNVMVLMLIPTNKCHWENFVGRHIIGYDIRNRNQTNYYKMRKKLFWKNWFGNGDYIDVLPMFWLMPDVMWCCCFFKPIKRWHEHNTIERSDCMIEMILPVDTMKELYPMPEETTPFFWRYWRRQTHAFDCCRTKIGGFQFNGLYGHSDWWPKKEKYHFHWDVLFAGNESKMMWNDSMRQIVIMHNGFALSQTSDVWLQPVVHRRDVRKESHSLMEMVRHNAMDDFFDAYVRNFSTQRAGTQPFFDAFKEDQIAHYVGNWRLSFDKKGWCFNRHAIAYVSNQAHIPHLFDRRSKQGALHDVVNGHRWMYGLVKSQMVREQEHTRNSFYFFETCYNLRAKTPMHQMFYKTFDTADRDDALPLTDYEHACMKNGLIGWYYLHQMAHISEDAAFIIWHKFVQFGYFEKSGDFWAYCYPHGGIWVLELPYKGEMMIIPDFCEVYISYRVVFIYIGKGLCHMSLSKMMSSQHYQWGNMCIRMLVCQRRCDAAWRHCITSNIVGECHPHNKIDAEHSKIDSLNYVDIYFPMIRKWWYWCNYSWDIGRWMSKSMVDWLHHMAPNFYTVVWFDYMHIMLSGKCCEYKCNWPHWNKLRRKMPKACAFNFTYIDMRGKIRFESFHDWSEKPMFDNDCCSMHDHERCK')
