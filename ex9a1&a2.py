import math

from functools import lru_cache


w1, w2 = "night", "macht"


def jaccard(a, b):

    return len(set(a) & set(b)) / len(set(a) | set(b))


def cosine(a, b):

    c = set(a + b)

    v1 = [a.count(x) for x in c]

    v2 = [b.count(x) for x in c]


    dot_product = sum(x * y for x, y in zip(v1, v2))

    mag1 = math.sqrt(sum(x**2 for x in v1))

    mag2 = math.sqrt(sum(y**2 for y in v2))


    return dot_product / (mag1 * mag2) if mag1 * mag2 != 0 else 0



print(f"Comparing '{w1}' and '{w2}':")
print(f" - Jaccard: {jaccard(w1, w2):.4f}")
print(f" - Cosine: {cosine(w1, w2):.4f}")