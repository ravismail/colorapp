import os
import sys
from chromadb import HttpClient
from langchain_community.document_loaders import PyPDFLoader, UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama import OllamaEmbeddings
from chromadb.config import Settings
from langchain_core.documents import Document
import chromadb

# ---- CONFIG ----
PDF_PATH = "C:\\Users\\ravis\\Documents\\langchain\\Course\\Sampleproject\\RAG\\Terraformnotes.pdf"  # update this
CHROMA_COLLECTION = "pdf_collection"
CHROMA_HOST = "localhost"
CHROMA_PORT = 8000

# ---- VERIFY FILE ----
if not os.path.exists(PDF_PATH):
    raise FileNotFoundError(f"❌ File not found at: {PDF_PATH}")
print(f"✅ Found PDF: {PDF_PATH}")

# ---- LOAD PDF ----
loader = PyPDFLoader(PDF_PATH)
documents = loader.load_and_split()
print(f"✅ Loaded {len(documents)} pages")

# ---- SPLIT ----
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

#chunks = [Document(page_content=text) for text in chunks]
chunks = splitter.split_documents(documents)
print(f"✅ Split into {len(chunks)} chunks")

# Metada

final_chunks=[]
for i, chunk in enumerate(chunks):
    if not isinstance(chunk, Document):
        chunk = Document(page_content=chunk)
    if not chunk.metadata:
        chunk.metadata = {"chunk_id": i, "source": os.path.basename(PDF_PATH)}
    final_chunks.append(chunk)

    #print(f"✅ Prepared {len(final_chunks)} Document objects with metadata")
# ---- LOCAL EMBEDDINGS VIA OLLAMA ----
#embeddings = OllamaEmbeddings(model="ai/nomic-embed-text-v1.5", base_url="http://localhost:12434/engines/llama.cpp/v1")
embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url="http://localhost:11434")
# ---- CONNECT TO CHROMA ----
try:
    chroma_client = HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    vectorstore = Chroma(
        client=chroma_client,
        collection_name=CHROMA_COLLECTION,
        embedding_function=embeddings
    )
    print(f"✅ Connected to Chroma at {CHROMA_HOST}:{CHROMA_PORT}")
except Exception as e:
    print("❌ Failed to connect to Chroma.", e)
    sys.exit(1)

    #raise ConnectionError(f"❌ Could not connect to Chroma at {CHROMA_HOST}:{CHROMA_PORT}. Error: {e}")

# ---- EMBED & STORE IN CHROMA

# --add documents to chroma

try:
    vectorstore.add_documents(final_chunks)
    print(f"✅ Embedded and stored {len(final_chunks)} chunks in '{CHROMA_COLLECTION}'")
except Exception as e:
    print("❌ Failed to add documents to Chroma.----", e)
    sys.exit(1)

    #raise RuntimeError(f"❌ Failed to add documents to Chroma. Error: {e}")

######
#chroma_client = HttpClient(host="localhost", port=8000)
#vectorstore = Chroma(
#    client=chroma_client,
#    collection_name=CHROMA_COLLECTION,
#    embedding_function=embeddings
#)
#print(f"✅ Embedded and stored {len(chunks)}")
# ---- ADD TO CHROMA ----
#vectorstore.add_documents(chunks)

#print(f"✅ Embedded and stored {len(chunks)} chunks in '{CHROMA_COLLECTION}'")
