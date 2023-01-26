

def tokenized_txt(x):
    x = x.replace(",", " ")
    x = x.replace("\'s", " ")
    x = x.replace("?", " ")
    x = x.replace(".", " ")
    x = x.replace("!", " ")
    x = x.split(" ")
    for i in x:
        if i == "":
            x.remove(i)
    return x


def count_ngrams(x,n):
    L = []
    for i in range(len(x)-n+1):
        L.append(x[i:i+n])
    D = {}
    for j in range(len(L)):
        D.update({L[j] : L.count(L[j])})
    return D


