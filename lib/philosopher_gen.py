import random

def markov_text(s,n,seed, length = 10):
    text_so_far = seed
    L = []
    for i in range(len(s)-n+2):
        L.append(s[i:i+n+1])
    k = 0

    while len(text_so_far) <= length:
        A = []

        most_recent = text_so_far[-n:]

        for j in range(len(L)):
            if L[j][0:n] == most_recent:
                A.append(L[j])

        a = list(set(A))
        D = {}

        for i in range(len(a)):
            D.update({a[i] : L.count(a[i])})
        value = list(D.values())
        sumhh = sum(value)
        B = []

        for m in range(len(value)):
            B.append(value[m]/sumhh)

        options = a
        weights = B
        text = random.choices(options, weights)
        text1 = text[0][-1]

        text_so_far = text_so_far + text1
    return text_so_far

def philosopher_text(philosopher, n, length, df):
    s =  philosopher + " said:"
    for i in range(100):
        s = s + df.sentence_lowered[df.author == philosopher].reset_index().sentence_lowered[i]
    return markov_text(s, n, philosopher + " said:", length)