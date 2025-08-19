import re
from collections import defaultdict

corpus = [
    "the cat sat on the mat.",
    "the dog lay on the rug.",
]

vocab = defaultdict(int)

for sentence in corpus:
    words = re.findall(r"\b\w+\b", sentence.lower())
    for word in words:
        vocab[word] += 1

sorted_vocab = dict(sorted(vocab.items(), key=lambda x: x[1], reverse=True))
print("Vocabulary with Frequencies:", sorted_vocab)
