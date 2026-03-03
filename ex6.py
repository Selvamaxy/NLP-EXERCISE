from collections import defaultdict
corpus = ["hello welcome", " to kcet"]
bigram = defaultdict(int)
unigram = defaultdict(int)
vocab = set()
for s in corpus:
    w = s.split()
    vocab.update(w)
    for i in range(len(w)-1):
        unigram[w[i]] += 1
        bigram[(w[i], w[i+1])] += 1
V = len(vocab)
prob = (bigram[("love","python")] + 1) / (unigram["love"] + V)
print(round(prob, 2))