# File input/output



def read_fasta(filename):
    f = open(filename,'r')
    names = []
    genome = []
    counter = -1
    for line in f:
        if line[0]==">":
            
            counter += 1
            
            names.append(line[1:].strip())
            genome.append([])
            
        else:
            genome[counter].append(line.strip())
   
    return names, genome

names, genome = read_fasta("drosophila_genome.fa")






