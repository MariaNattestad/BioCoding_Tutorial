

def reverse_complement(DNA):
    DNA = DNA.upper()
    
    complement = []
    
    complement_dictionary = {
    "A":"T", 
    "T":"A", 
    "G":"C",
    "C":"G"
    }
    
    for base in DNA:
        complement.append(complement_dictionary.get(base,"N"))
        
    return complement


DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#DNA = raw_input('Enter your DNA: ')
print reverse_complement(DNA)