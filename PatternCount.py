# Pandu's PatternCount algorithm for genetics stuff
# Just counts how many times Pattern repeats in Dna
# Dead simple

def PatternCount(Dna, Pattern):
    # fill in your function here
    count=0
    x=0
    while x<(len(Dna)-len(Pattern)+1):
        if Text[x:(x+len(Pattern))]==Pattern:
                count=count+1
        x=x+1
    return count




