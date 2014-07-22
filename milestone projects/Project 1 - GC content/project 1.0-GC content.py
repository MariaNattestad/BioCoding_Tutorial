DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"


AT = 0
GC = 0
for base in DNA:
    if base=="A" or base=="T":
        AT = AT+1
        # AT += 1
    elif base=="G" or base=="C":
        GC = GC+1
        # GC += 1

GC_percentage = 100*float(GC)/float(GC+AT)
#GC_percentage = 100.0*GC/GC+AT

print "The GC content of the input string is %f" % (GC_percentage)

