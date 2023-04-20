s = 'I am an NLPer'
words = s.split()

def make_n_gram(s,n):
    return [(s[i],s[i+1]) for i in range(len(s)-1)]

print(make_n_gram(s, 2))

print(make_n_gram(words, 2))
