# a simple clump finder.
def ClumpFinding(genome, k, L, t):
    clumps = []
    for i in range(0, len(genome), k):# stride k speeds it up
        split_words = {}
        length  = genome[i:L+i]
        for j in range(len(length)):
            pattern = length[j:k+j]
            try:
                split_words[pattern] += 1
            except KeyError:
                split_words[pattern] = 1
        to_add = [k for k, val in split_words.items() if t  == val]
        clumps += to_add
    return set(clumps)



