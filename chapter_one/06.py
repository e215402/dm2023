s1 = ''
s2 = ''

def make_n_gram(s,n):
    return [(s[i],s[i+1]) for i in range(len(s)-1)]
