import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load documents
with open("data/cdp_docs.json", "r") as f:
    DOCS = json.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create FAISS index
doc_texts = list(DOCS.values())
doc_embeddings = model.encode(doc_texts)
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(np.array(doc_embeddings))

def get_cdp_answer(question):
    question_embedding = model.encode([question])
    _, I = index.search(np.array(question_embedding), 1)
    best_match = doc_texts[I[0][0]]
    return best_match
