import getpass
import os

from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")


# model = ChatOpenAI(model="gpt-4o-mini")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = Chroma(
    collection_name="products_collection",
    embedding_function=embeddings,
    persist_directory="./db/langchain_chroma",
)

results = vector_store.similarity_search(
    "negative",
    k=2,
    filter={"source": "tweet"},
)
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")
