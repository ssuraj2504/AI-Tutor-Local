# AI Tutor Local - Phase 2 🚀

A standalone local AI Tutor app with **subject-wise organization** and **automatic YouTube video suggestions**. No external APIs required!

## ✨ New Features (Phase 2)

- 📁 **Subject-wise organization** - Organize PDFs by subject (OS, DBMS, CN, etc.)
- 🔍 **Automatic FAISS indexing** per subject
- 🎥 **YouTube video suggestions** for each answer
- 💬 **Multi-subject chat** - Choose subject, then ask questions
- 📚 **Smart source tracking** with PDF names

## Setup

1. **Create virtual environment:**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Organize your PDFs:**
   - Put PDFs in subject folders: `subject_pdfs/OS/`, `subject_pdfs/DBMS/`, etc.
   - Example structure:
     ```
     subject_pdfs/
     ├── OS/
     │   ├── Lec1.pdf
     │   └── Lec2.pdf
     ├── DBMS/
     │   └── Notes.pdf
     └── CN/
         └── CN_Lec1.pdf
     ```

4. **Start chatting:**
   ```bash
   python chat.py
   ```

## Usage

1. **Choose a subject** (e.g., OS, DBMS, CN)
2. **Ask questions** about that subject
3. **Get answers** with sources and YouTube video suggestions
4. **Type 'exit'** to change subjects or quit

## Example Session

```
📘 Enter subject (e.g., OS, DBMS, CN): DBMS

You (DBMS): Explain normalization in databases

Tutor: Normalization is a process of organizing data in a database...

📚 Sources: ['DBMS_Notes.pdf']

🎥 Recommended YouTube Videos:
- Database Normalization Explained: https://youtube.com/...
- 1NF 2NF 3NF Simplified: https://youtube.com/...
```

## File Structure

```
AI_Tutor_Local/
├── subject_pdfs/         # Organize PDFs by subject
│   ├── OS/              # Operating Systems PDFs
│   ├── DBMS/            # Database Management PDFs
│   └── CN/              # Computer Networks PDFs
├── indexes/             # Auto-generated FAISS indexes
├── local_rag.py         # Subject-wise RAG implementation
├── youtube_search.py    # YouTube video suggestions
├── chat.py              # Multi-subject chatbot
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Models Used

- **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2` (fast on CPU)
- **Text Generation:** `google/flan-t5-base`
- **YouTube Search:** `youtube-search-python` (free, no API key)

## Notes

- **First run** downloads models (~1-2GB)
- **Indexes are built automatically** when you first ask about a subject
- **All processing is local** - no internet required after setup
- **YouTube suggestions** require internet connection
