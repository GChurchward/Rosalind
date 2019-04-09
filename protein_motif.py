"""

a script to take a list of proteins from a txt file, access UniProt protein database and search for a certain
protein motif
    rosalind MPRT
"""
from pip._vendor import urllib3


def file_open_to_list(file_path):
    """

    :param file_path:
    :return:
    """
    proteins_id_list =[]
    protein_dict = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            proteins_id_list.append(line)

    print(proteins_id_list)
    http = urllib3.PoolManager()
    for item in proteins_id_list:
        url = 'http://www.uniprot.org/uniprot/' + item + '.fasta'
        req = http.request("GET", url)
        # print(req)
        string = req.data.decode('utf-8')
        # print(string)
        protein_dict[item] = string

        print(protein_dict)


file_open_to_list('/Users/Glen/Documents/protein_id_list.txt')