from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')
word1, word2 = "night", "macht"
emb1 = model.encode(word1, convert_to_tensor=True)
emb2 = model.encode(word2, convert_to_tensor=True)
similarity = util.cos_sim(emb1, emb2)
print(f"BERT Similarity: {similarity.item():.4f}")
model = SentenceTransformer('all-distilroberta-v1')
w1, w2 = "night", "macht"
emb1 = model.encode(w1, convert_to_tensor=True)
emb2 = model.encode(w2, convert_to_tensor=True)
similarity = util.cos_sim(emb1, emb2)
print(f"RoBERTa Similarity: {similarity.item():.4f}")