

# make it work with RNA as well

def calc_GC_content(DNA):
    DNA = DNA.upper()
    
    AT = 0
    GC = 0
    for base in DNA:
        if base=="A" or base=="T" or base=="U":
            AT = AT+1
            # AT += 1
        elif base=="G" or base=="C":
            GC = GC+1
            # GC += 1
        else:
            print "The letter %s does not belong in DNA and was not counted" % (base)
    
    if AT+GC == 0:
        print "no nucleotides"
        return 0 # always return something so you don't get an eror
    else:
        GC_percentage = 100*float(GC)/float(GC+AT)
        #GC_percentage = 100.0*GC/GC+AT
        return GC_percentage







DNA = raw_input('Enter your DNA: ')
print calc_GC_content(DNA)
