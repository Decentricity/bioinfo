# Pandu's FrequentWords function
# From a genetic Text, returns a list of k-mers that most often appear

def FrequentWords(Text, k):
    a=0
    b=0
    c=0
    x=""
    y=[]
    z=[]
    r=[]
    while a<(len(Text)-k+1):
        x=Text[a:a+k]
        
        b=0
        c=0
        while b<len(Text):
            if x==Text[b:b+k]:
                c=c+1
            b=b+1
        z.append(c)

        y.append(x)
        a=a+1
    max=z[0]
    i=0
    while i<len(z):
        if z[i]>max:
            max=z[i]
        i=i+1
    i=0

    while i<len(z):
        if z[i]==max:
            
            r.insert(0,y[i]) 
        i=i+1
    r = list(dict.fromkeys(r))

    return(r)




