import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✅ Requirements installed!")

def launch_app():
    """Launch the Streamlit app"""
    print("🚀 Launching AI Tutor Web Interface...")
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    print("🎓 AI Tutor Local - Final Year Project")
    print("=" * 50)
    
    # Check if requirements are installed
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit not found, installing requirements...")
        install_requirements()
    
    # Launch the app
    launch_app()
