import json

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = Chroma(
    collection_name="products_collection",
    embedding_function=embeddings,
    persist_directory="./db/langchain_chroma",
)


def load_products():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data["products"]

    except FileNotFoundError:
        print("Error: File not found")
        return []

    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return []


def create_documents(products):
    documents = []
    for product in products:
        try:
            content = f"""
            Name: {product['details']['name']}
            Description: {product['details']['description']}
            Link: {product['link']}
            """

            doc = Document(
                page_content=content.strip(),
                metadata={
                    "product_id": product["id"],
                    "name": product["details"]["name"],
                    "image_url": product["details"]["image"],
                    "product_link": product["link"],
                },
            )
            documents.append(doc)

        except KeyError as e:
            print(f"Error: Missing key in product data: {e}")
            continue

    return documents


def add_products_to_chroma():
    products = load_products()

    if not products:
        print("No products to add")
        return

    documents = create_documents(products)

    if documents:
        try:
            vector_store.add_documents(documents=documents, ids=[str(i) for i in range(10)])
            print(
                f"Successfully added {len(documents)} products to Chroma vector store"
            )

        except Exception as e:
            print(f"Error adding documents to vector store: {e}")

    else:
        print("No valid documents created")


if __name__ == "__main__":
    add_products_to_chroma()
