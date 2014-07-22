
DNA = raw_input('Enter your DNA: ')

DNA = DNA.upper()

AT = 0
GC = 0
for base in DNA:
    if base=="A" or base=="T":
        AT = AT+1
        # AT += 1
    elif base=="G" or base=="C":
        GC = GC+1
        # GC += 1
    else:
        print "The letter %s does not belong in DNA and was not counted" % (base)

if AT+GC == 0:
    print "no nucleotides"
else:
    GC_percentage = 100*float(GC)/float(GC+AT)
    #GC_percentage = 100.0*GC/GC+AT
    print "The GC content of the input string is %f" % (GC_percentage)







# give inputs that their code should be able to handle:
# AGCGATN
# cgatcga
# SLKFSLDKFJS
