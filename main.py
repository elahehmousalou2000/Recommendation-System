from sklearn.metrics.pairwise import cosine_similarity

items = [
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1],
]

scores = cosine_similarity([items[0]], items)[0]

for i, score in enumerate(scores):
    print(f"Item {i}: {score:.3f}")
