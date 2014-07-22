

def reverse_complement(DNA):
    DNA = DNA.upper()
    
    complement = str()
    
    complement_dictionary = {
    "A":"T", 
    "T":"A", 
    "G":"C",
    "C":"G"
    }
    
    for base in DNA:
        complement+=complement_dictionary.get(base,"N")
    
    revcomp = complement[::-1]
    return revcomp


DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#DNA = raw_input('Enter your DNA: ')
print reverse_complement(DNA)


