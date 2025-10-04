# AI Tutor Local - Final Year Project 🎓

A comprehensive **AI-powered study assistant** with **modern web interface**, **subject-wise organization**, and **automatic YouTube video suggestions**. Perfect for final year projects!

## ✨ Features

### 🖥️ **Modern Web Interface**
- Beautiful, responsive Streamlit UI
- Real-time chat interface
- Subject selection with visual indicators
- YouTube video integration
- Project statistics dashboard

### 🧠 **AI-Powered Learning**
- Advanced RAG (Retrieval-Augmented Generation) system
- Local processing - no external APIs required
- Smart context understanding
- Source citation with PDF references

### 📁 **Subject Organization**
- Organize PDFs by subjects (OS, DBMS, CN, etc.)
- Automatic FAISS indexing per subject
- Easy subject switching
- Visual PDF management

### 🎥 **Enhanced Learning**
- Automatic YouTube video suggestions
- Relevant educational content
- Direct video links
- Integrated learning experience

### 🔒 **Privacy & Security**
- All processing happens locally
- No data sent to external servers
- Complete privacy protection
- Offline capability

## 🚀 Quick Start

### Option 1: Web Interface (Recommended)
```bash
# Install dependencies
pip install -r requirements.txt

# Launch web interface
streamlit run app.py
```

### Option 2: Terminal Interface
```bash
# Install dependencies
pip install -r requirements.txt

# Start terminal chat
python chat.py
```

### Option 3: Auto-Launcher
```bash
# Install and launch automatically
python launch.py
```

## 📁 Project Structure

```
AI_Tutor_Local/
├── app.py                  # 🌐 Streamlit web interface
├── launch.py               # 🚀 Auto-launcher script
├── chat.py                 # 💬 Terminal chatbot
├── local_rag.py            # 🧠 RAG implementation
├── youtube_search.py       # 🎥 YouTube integration
├── subject_pdfs/           # 📚 Organized PDFs by subject
│   ├── OS/                # Operating Systems
│   ├── DBMS/              # Database Management
│   └── CN/                # Computer Networks
├── indexes/               # 🔍 Auto-generated FAISS indexes
├── requirements.txt       # 📦 Dependencies
└── README.md             # 📖 This file
```

## 🎯 Usage Examples

### Web Interface
1. **Launch:** `streamlit run app.py`
2. **Select Subject:** Choose from sidebar (OS, DBMS, CN)
3. **Ask Questions:** Type in the chat interface
4. **Get Answers:** AI responses with sources and videos
5. **Explore:** Use the dashboard for project insights

### Terminal Interface
1. **Launch:** `python chat.py`
2. **Select Subject:** Type subject name (e.g., "OS")
3. **Ask Questions:** Natural language queries
4. **Get Responses:** Answers with sources and YouTube links

## 🛠️ Technical Stack

### **AI Models**
- **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2`
- **Text Generation:** `google/flan-t5-base`
- **Vector Store:** FAISS (Facebook AI Similarity Search)

### **Web Technologies**
- **Frontend:** Streamlit
- **Backend:** Python, LangChain
- **PDF Processing:** PyPDF2
- **Video Search:** youtube-search-python

### **Architecture**
- **RAG System:** Retrieval-Augmented Generation
- **Local Processing:** No external API dependencies
- **Modular Design:** Subject-wise organization
- **Scalable:** Easy to add new subjects

## 📊 Project Highlights

- ✅ **Modern Web UI** with responsive design
- ✅ **AI-Powered** intelligent responses
- ✅ **Subject Organization** for better learning
- ✅ **YouTube Integration** for enhanced learning
- ✅ **Privacy-First** local processing
- ✅ **Professional Documentation** for final year projects
- ✅ **Easy Setup** with automated installation
- ✅ **Cross-Platform** compatibility

## 🎓 Perfect for Final Year Projects

This project demonstrates:
- **Advanced AI/ML concepts** (RAG, embeddings, transformers)
- **Modern web development** (Streamlit, responsive UI)
- **Software architecture** (modular design, separation of concerns)
- **User experience** (intuitive interface, real-time interaction)
- **Technical documentation** (comprehensive README, code comments)

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ssuraj2504/AI-Tutor-Local.git
   cd AI-Tutor-Local
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your PDFs:**
   - Place PDFs in appropriate subject folders
   - Example: `subject_pdfs/OS/Lecture1.pdf`

5. **Launch the application:**
   ```bash
   streamlit run app.py
   ```

## 📝 Notes

- **First run** downloads AI models (~1-2GB)
- **Indexes are built automatically** when you first ask about a subject
- **YouTube suggestions** require internet connection
- **All AI processing** happens locally for privacy
- **Web interface** runs on `http://localhost:8501`

## 🤝 Contributing

This is a final year project, but contributions are welcome! Feel free to:
- Add new features
- Improve the UI/UX
- Optimize performance
- Add more AI models

## 📄 License

This project is open source and available under the MIT License.

---

**🎓 Final Year Project by Suraj**  
**GitHub:** https://github.com/ssuraj2504/AI-Tutor-Local
