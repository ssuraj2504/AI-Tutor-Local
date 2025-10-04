import streamlit as st
import os
import time
from local_rag import generate_answer
from youtube_search import get_youtube_links
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="AI Tutor Local - Final Year Project",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern design
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    
    .user-message {
        background-color: #f0f2f6;
        margin-left: 2rem;
    }
    
    .tutor-message {
        background-color: #e8f4fd;
        margin-right: 2rem;
    }
    
    .youtube-card {
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    
    .stSelectbox > div > div {
        background-color: #f8f9fa;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_subject" not in st.session_state:
    st.session_state.current_subject = None
if "subjects" not in st.session_state:
    st.session_state.subjects = []

def get_available_subjects():
    """Get list of available subjects from subject_pdfs folder"""
    subjects = []
    pdf_dir = Path("subject_pdfs")
    if pdf_dir.exists():
        for folder in pdf_dir.iterdir():
            if folder.is_dir() and any(folder.glob("*.pdf")):
                subjects.append(folder.name)
    return subjects

def display_youtube_videos(videos):
    """Display YouTube videos in a nice format"""
    if not videos:
        return
    
    st.markdown("### 🎥 Recommended YouTube Videos")
    for i, video in enumerate(videos, 1):
        with st.container():
            st.markdown(f"""
            <div class="youtube-card">
                <h4>📺 {video['title']}</h4>
                <p><a href="{video['link']}" target="_blank">🔗 Watch Video</a></p>
            </div>
            """, unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🎓 AI Tutor Local</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Final Year Project - Intelligent Study Assistant</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 📚 Project Features")
        st.markdown("""
        <div class="feature-card">
            <h3>🧠 AI-Powered Learning</h3>
            <p>Advanced RAG system with local processing</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>📁 Subject Organization</h3>
            <p>Organized by subjects (OS, DBMS, CN)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🎥 Video Suggestions</h3>
            <p>Automatic YouTube recommendations</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🔒 Privacy First</h3>
            <p>All processing happens locally</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Subject selection
        st.markdown("---")
        st.markdown("## 📘 Select Subject")
        
        # Get available subjects
        subjects = get_available_subjects()
        if not subjects:
            st.warning("No subjects found! Add PDFs to subject_pdfs folder.")
            st.markdown("### 📁 Folder Structure:")
            st.code("""
            subject_pdfs/
            ├── OS/
            │   ├── Lec1.pdf
            │   └── Lec2.pdf
            ├── DBMS/
            │   └── Notes.pdf
            └── CN/
                └── CN_Lec1.pdf
            """)
        else:
            selected_subject = st.selectbox(
                "Choose a subject:",
                ["Select a subject..."] + subjects,
                key="subject_selector"
            )
            
            if selected_subject != "Select a subject...":
                st.session_state.current_subject = selected_subject
                st.success(f"Selected: {selected_subject}")
                
                # Show PDFs in this subject
                pdf_dir = Path(f"subject_pdfs/{selected_subject}")
                pdf_files = list(pdf_dir.glob("*.pdf"))
                if pdf_files:
                    st.markdown(f"**📄 PDFs in {selected_subject}:**")
                    for pdf in pdf_files:
                        st.markdown(f"• {pdf.name}")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## 💬 AI Tutor Chat")
        
        if not st.session_state.current_subject:
            st.info("👈 Please select a subject from the sidebar to start chatting!")
        else:
            # Chat interface
            st.markdown(f"**Currently chatting about: {st.session_state.current_subject}**")
            
            # Display chat history
            for message in st.session_state.messages:
                if message["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>You:</strong> {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message tutor-message">
                        <strong>AI Tutor:</strong> {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Show sources
                    if "sources" in message:
                        st.markdown(f"**📚 Sources:** {', '.join(message['sources'])}")
                    
                    # Show YouTube videos
                    if "videos" in message:
                        display_youtube_videos(message["videos"])
            
            # Chat input
            if prompt := st.chat_input("Ask a question about your study material..."):
                # Add user message
                st.session_state.messages.append({"role": "user", "content": prompt})
                
                # Generate AI response
                with st.spinner("🤔 AI Tutor is thinking..."):
                    try:
                        answer, sources = generate_answer(prompt, st.session_state.current_subject)
                        videos = get_youtube_links(prompt)
                        
                        # Add AI response
                        st.session_state.messages.append({
                            "role": "assistant", 
                            "content": answer,
                            "sources": sources,
                            "videos": videos
                        })
                        
                        # Rerun to show new messages
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
                        st.session_state.messages.append({
                            "role": "assistant", 
                            "content": "Sorry, I encountered an error. Please try again."
                        })
                        st.rerun()
    
    with col2:
        st.markdown("## 📊 Project Statistics")
        
        # Show project stats
        subjects = get_available_subjects()
        total_pdfs = 0
        for subject in subjects:
            pdf_dir = Path(f"subject_pdfs/{subject}")
            total_pdfs += len(list(pdf_dir.glob("*.pdf")))
        
        st.metric("📚 Total Subjects", len(subjects))
        st.metric("📄 Total PDFs", total_pdfs)
        st.metric("💬 Chat Messages", len(st.session_state.messages))
        
        # Clear chat button
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("---")
        st.markdown("## 🛠️ Technical Details")
        st.markdown("""
        **Models Used:**
        - Embeddings: all-MiniLM-L6-v2
        - Text Generation: google/flan-t5-base
        - Vector Store: FAISS
        
        **Technologies:**
        - Python, Streamlit
        - LangChain, Transformers
        - YouTube Search API
        """)
        
        st.markdown("---")
        st.markdown("## 📝 Project Info")
        st.markdown("""
        **Final Year Project**
        
        **Student:** Suraj
        
        **Features:**
        ✅ Local AI Processing
        ✅ Subject-wise Organization  
        ✅ YouTube Integration
        ✅ Modern Web Interface
        ✅ Privacy-focused Design
        """)

if __name__ == "__main__":
    main()
