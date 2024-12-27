from uuid import uuid4

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = Chroma(
    collection_name="products_collection",
    embedding_function=embeddings,
    persist_directory="./db/langchain_chroma",  
)

print("adding docs")

vector_store.add_documents(
    documents=[
        Document(
            page_content="I have a bad feeling I am going to get deleted :(",
            metadata={"source": "tweet"},
            id=10,
        )
    ],
    ids=["101-101"],
)

print("done")
