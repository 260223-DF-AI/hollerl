from langchain_community.vectorstores import FAISS
from langchain_core import documents
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereRerank
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import faiss

# =====================================================================
# 1. Initialize Embeddings
# =====================================================================
# TODO: Create a BedrockEmbeddings instance.

embeddings = OllamaEmbeddings(
    model="llama3.2"
)

# =====================================================================
# 2. Create the Vector Store
# =====================================================================
# TODO: Use PineconeVectorStore to connect to your Pinecone index.
# Use index_name="your-index-name" and the embeddings from above.
# PINECONE_API_KEY must be in your environment.


# =====================================================================
# 3. Add Sample Documents (Run Only Once!)
# =====================================================================
sample_docs = [
    Document(page_content="Full-time employees receive 20 days of Paid Time Off per year.", metadata={"topic": "pto"}),
    Document(page_content="PTO must be requested 2 weeks in advance through the HR portal.", metadata={"topic": "pto"}),
    Document(page_content="Unused PTO of up to 5 days may be rolled over to the next calendar year.", metadata={"topic": "pto"}),
    Document(page_content="The company 401k match is 4% with a 2-year vesting schedule.", metadata={"topic": "benefits"}),
    Document(page_content="Remote work is permitted up to 3 days per week with manager approval.", metadata={"topic": "remote"}),
]

vector_store = FAISS.from_documents(
    documents=sample_docs,
    embedding=embeddings
)

# TODO: Uncomment to upsert documents into Pinecone (run once only)
#vector_store.add_documents(sample_docs)

# =====================================================================
# 4. Build the Two-Stage Retrieval Pipeline
# =====================================================================
# TODO: Create a base retriever from the vectorstore using .as_retriever().
# Use search_kwargs={"k": 5} to recall the top 5 candidates.

#retriever = vector_store.as_retriever(
#    search_kwargs={"k": 2}
#)
# TODO: Create a CohereRerank compressor with top_n=2 to return top 2 results.
# Wrap it in a ContextualCompressionRetriever.

# =====================================================================
# 5. Query and Display
# =====================================================================
def run_exercise():
    print("=== e042: Optimizing Vector Retrieval ===\n")
    query = "How many vacation days do I get per year?"
    
    # TODO: Invoke your retriever with the query above.
    # Print each result's relevance_score (from metadata) and page_content.
    print(f"Query: {query}\n")

    # Invoke retriever
    #results = retriever.invoke(query)
    results = vector_store.similarity_search_with_score(query, k=5)

    # Display results
    for i, (doc, score) in enumerate(results, 1):
        print(f"Result {i}:")
        print(f"Relevance Score: {score}")
        print(f"Content: {doc.page_content}\n")

if __name__ == "__main__":
    run_exercise()
