"""

a script to take a list of proteins from a txt file, access UniProt protein database and search for a certain
protein motif

To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means
"either X or Y" and {X} means "any amino acid except X."
For example, the N-glycosylation motif is written as N{P}[ST]{P}
    rosalind MPRT
"""
import requests


def protein_strip(request_string):
    """

    :param request_string: the string for a protein from a resquest from uniprot
    :return: a clean protein string
    """
    # print(request_string)
    protein = []
    final_protein = ''
    for value in str(request_string):
        protein.append(value)
        # print(value)
    # print(protein)
    protein_concat = []
    for index, value in enumerate(protein):
        # print(f' this is i {index}')
        if value == '\\':
            # print(protein[index + 1:])
            protein_concat.append(protein[index + 2:])
    # print(protein_concat)
    protein_concat = protein_concat[0]
    # print(protein_concat)
    for acid in protein_concat:
        if acid == '\\':
            pass
        elif acid == "'":
            pass
        elif acid == 'n':
            pass
        else:
            final_protein += acid
    # print(final_protein)
    return final_protein


def file_open_to_list(file_path):
    """

    :param file_path: file path location of a text file with a list of protein names
    :return: dictionary of proteins from uniprot and the corresponding protein
    """
    proteins_id_list = []
    protein_dict = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            proteins_id_list.append(line)

    # print(proteins_id_list)
    for item in proteins_id_list:
        url = 'http://www.uniprot.org/uniprot/' + item + '.fasta'
        req = requests.get(url)
        # print(req)
        string = req.content
        # print(string)
        protein_dict[item] = protein_strip(string)
    # print(protein_dict)
    return protein_dict


def protein_motif_search(file_path):
    protein_dict = file_open_to_list(file_path)
    print(protein_dict)
    for key, value in protein_dict.items():
        # print(key)
        # print(value)
        # print(protein_dict[key])
        locations = ''
        for index in range(0, len(value)):
            # print(index)
            if ((protein_dict[key][index] == 'N')
                    and ((protein_dict[key][index + 1]) != 'P')
                    and ((protein_dict[key][index + 2]) == 'S' or (protein_dict[key][index + 2]) == 'T')
                    and ((protein_dict[key][index + 3]) != 'P')):
                locations += (str(index + 1) + ' ')
        if len(locations) > 0:
            print(key)
            print(locations)
        else:
            pass



protein_motif_search('/Users/Glen/Downloads/rosalind_mprt.txt')

# file_open_to_list('A2Z669')
