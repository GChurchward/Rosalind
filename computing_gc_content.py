#TODO split text via >
#TODO create dictionary using defined string length
#TODO link to the DNA string
#TODO calculate GC content of DNA string
#TODO equate value to dictionary
#TODO move through dictionary looking for highest and return highest string and GC content


def file_open(file_path):
    var = []
    fasta = []
    with open(file_path, 'r') as f:
        g = f.read()
        for line in g:
            var.append(line)
    print(var)
    #chevron = var.index('>')
    chevron = [i for i, x in enumerate(var) if x == ">" or x == "\n"]
    print(chevron)

    print(var)
    x = []
    y = chevron[0:1]
    x.append((var[y]))
    print(x)




file_open('/Users/Glen/PycharmProjects/Rosalind/test_case.txt')