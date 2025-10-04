# local_rag.py
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

MODEL_NAME = "google/flan-t5-base"

print("🔹 Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

INDEX_DIR = "indexes"
PDF_DIR = "subject_pdfs"

def build_or_load_index(subject):
    os.makedirs(INDEX_DIR, exist_ok=True)
    index_path = os.path.join(INDEX_DIR, f"{subject}.faiss")
    pdf_path = os.path.join(PDF_DIR, subject)
    if not os.path.exists(pdf_path):
        print(f"❌ No notes found for {subject}. Add PDFs to {pdf_path}")
        return None

    if os.path.exists(index_path):
        print(f"✅ Loaded existing index for {subject}")
        return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    else:
        print(f"📘 Building new index for {subject}...")
        docs = []
        for file in os.listdir(pdf_path):
            if file.endswith(".pdf"):
                loader = PyPDFLoader(os.path.join(pdf_path, file))
                docs.extend(loader.load())

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)
        vectorstore = FAISS.from_documents(chunks, embeddings)
        vectorstore.save_local(index_path)
        print(f"✅ Index built for {subject} with {len(chunks)} chunks")
        return vectorstore

def generate_answer(query, subject):
    index = build_or_load_index(subject)
    if index is None:
        return "No index found for this subject.", []

    results = index.similarity_search(query, k=3)
    context = "\n".join([r.page_content for r in results])[:1500]
    prompt = f"Answer the following question based on the context:\n\nContext:\n{context}\n\nQuestion: {query}"

    output = generator(prompt, max_new_tokens=256)[0]['generated_text']
    sources = list({r.metadata['source'] for r in results})
    return output, sources