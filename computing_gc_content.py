#TODO split text via >
#TODO create dictionary using defined string length
#TODO link to the DNA string
#TODO calculate GC content of DNA string
#TODO equate value to dictionary
#TODO move through dictionary looking for highest and return highest string and GC content


def split_fasta(file_path):
    fasta = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                active_sequence_name = line[1:]
                if active_sequence_name not in fasta:
                    fasta[active_sequence_name] = []
                continue
            sequence = line
            fasta[active_sequence_name].append(sequence)

    #print(fasta)
    return fasta


def gc_content(f):
    x = split_fasta(f)
    gc_count = {}
    print(x)
    for key in x:
        for letter in key:
            if letter in ['G', 'C']:
                count += 1
                gc_count[key] = count
    return gc_count
    print(gc_count)


gc_content('/Users/Glen/PycharmProjects/Rosalind/test_case.txt')