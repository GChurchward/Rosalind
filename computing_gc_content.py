#TODO split text via >
#TODO create dictionary using defined string length
#TODO link to the DNA string
#TODO calculate GC content of DNA string
#TODO equate value to dictionary
#TODO move through dictionary looking for highest and return highest string and GC content


def file_open(file_path):
    var = []
    fasta = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                sequence_id = line[1:]
                # print(line)
                # print(sequence_id)
                if sequence_id not in fasta:
                    fasta[sequence_id] = ''
                    print(f'**** adding new key {sequence_id}', fasta)
            if not line.startswith('>'):
                sequence = line
                print(sequence)
                fasta[sequence_id] += sequence
                print(fasta)
            #sequence = line


#
file_open('C:/Users/gchurchward/Downloads/computing_gc_content.txt')