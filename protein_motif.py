"""

a script to take a list of proteins from a txt file, access UniProt protein database and search for a certain
protein motif
    rosalind MPRT
"""
import requests



def protein_strip(request_string):

    protein = []

    for i in request_string:
        protein.append(i)
        print(i)
    print(protein)
    protein_concat = []
    for i in protein:
        if i == '\n':
            protein_concat.append(protein[i + 1:])
            print(protein_concat)
         # line = i.strip()
        #print(line)
        # protein = []
        # if request_string[j: j + 1] == 'SV':
          #  print(line + 3)
            # for j in request_string:
            #     protein.append()
            # # protein = line[index:]
            # print(line)
            # # print(protein)


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
    for item in proteins_id_list:
        url = 'http://www.uniprot.org/uniprot/' + item + '.fasta'
        req = requests.get(url)
        # print(req)
        string = req.content
        # print(string)
        protein_dict[item] = string

        print(protein_dict)


# file_open_to_list('/Users/Glen/Documents/protein_id_list.txt')

protein_strip("b'>sp|A2Z669|CSPLT_ORYSI CASP-like protein 5A2 OS=Oryza sativa subsp. indica OX=39946 GN=OsI_33147 PE=3 SV=1\nMRASRPVVHPVEAPPPAALAVAAAAVAVEAGVGAGGGAAAHGGENAQPRGVRMKDPPGAP\nGTPGGLGLRLVQAFFAAAALAVMASTDDFPSVSAFCYLVAAAILQCLWSLSLAVVDIYAL\nLVKRSLRNPQAVCIFTIGDGITGTLTLGAACASAGITVLIGNDLNICANNHCASFETATA\nMAFISWFALAPSCVLNFWSMASR\n'")