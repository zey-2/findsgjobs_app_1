# chroma_setup.py
import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="chroma_jobs")

# local embedding model (no OpenAI needed, but you must `pip install sentence-transformers`)
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

jobs_collection = client.get_or_create_collection(
    name="findsg_jobs",
    embedding_function=embedding_fn,
)
