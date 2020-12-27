# Pandu's dead simple function to find the reverse complement of a gene strand.
def ReverseComplement(Pattern):
    a=0
    b=0
    c=""
    d=""
    while a<len(Pattern):
        if Pattern[a]=="A":
            d="T"
        elif Pattern[a]=="G":
            d="C"
        elif Pattern[a]=="T":
            d="A"
        elif Pattern[a]=="C":
            d="G"
        c=d+c
        a=a+1
    return c




