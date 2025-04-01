import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PyPDF2 import PdfReader
from htmlTemplates import css, bot_template, user_template

# Configure Streamlit page
st.set_page_config(
    page_title="Chat with Multiple PDFs",
    page_icon="📚",
    layout="wide"
)

def initialize_session_state():
    """Initialize session state variables"""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "pdf_content" not in st.session_state:
        st.session_state.pdf_content = ""

def get_pdf_text(pdf_docs):
    """Extract text from uploaded PDF documents"""
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
        except Exception as e:
            st.error(f"Error reading PDF {pdf.name}: {str(e)}")
            continue
    return text

def test_gemini_api():
    """Test API key validity before using the model"""
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
        response = model.generate_content("Test message for API verification")
        return response.text is not None  # API is working if it returns a response
    except Exception as e:
        st.error(f"API Error: {str(e)}")
        return False

def get_gemini_response(question):
    """Get response from Gemini model"""
    try:
        model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest')
        
        prompt = f"""
        Context: {st.session_state.pdf_content[:10000]}
        
        Question: {question}
        
        Please provide an answer based on the context provided. If the answer cannot be found in the context, 
        please say "I cannot find the answer to this question in the provided documents."
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def handle_user_input(user_question):
    """Process user input and display response"""
    if not st.session_state.pdf_content:
        st.warning("Please upload and process PDF documents first!")
        return

    # Add user question to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_question})
    
    # Get response from Gemini
    response = get_gemini_response(user_question)
    
    # Add response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.write(user_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)

def main():
    # Load environment variables
    load_dotenv()
    
    # Configure Google API
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        st.error("Google API Key not found! Please check your .env file.")
        st.stop()
    
    genai.configure(api_key=api_key)
    
    # Initialize session state
    initialize_session_state()
    
    # Add custom CSS
    st.write(css, unsafe_allow_html=True)
    
    # API Test
    with st.sidebar:
        st.title("📚 PDF Documents")
        if st.button("Test API Connection"):
            with st.spinner("Testing API..."):
                if test_gemini_api():
                    st.success("✅ API is working!")
                else:
                    st.error("❌ API test failed. Check your API key or project settings.")
    
    # Create sidebar
    with st.sidebar:
        # File uploader
        pdf_docs = st.file_uploader(
            "Upload your PDFs here",
            accept_multiple_files=True,
            type=['pdf']
        )
        
        # Process button
        if st.button("Process Documents"):
            if not pdf_docs:
                st.warning("Please upload PDF documents first!")
            else:
                with st.spinner("Processing documents..."):
                    try:
                        # Get PDF text
                        st.session_state.pdf_content = get_pdf_text(pdf_docs)
                        if st.session_state.pdf_content.strip():
                            st.success("Documents processed successfully!")
                        else:
                            st.error("No text could be extracted from the PDFs. Please make sure they are text-based PDFs.")
                    except Exception as e:
                        st.error(f"Error processing documents: {str(e)}")
    
    # Main page
    st.title("Chat with Multiple PDFs 📚")
    st.caption("Upload your PDFs and ask questions about them!")

    # User input
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_user_input(user_question)

if __name__ == '__main__':
    main()
