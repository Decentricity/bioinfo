# Pandu's pattern matching Python 3 function -- finds location of Pattern in the Genome.
def PatternMatching(Pattern, Genome):
    a=0
    b=0
    c=[]
    d=""
    while a<(len(Genome)+1):
        if Pattern==(Genome[a:(a+len(Pattern))]):
            c.append(a)
        a=a+1
    return c




