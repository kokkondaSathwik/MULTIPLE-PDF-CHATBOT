# Chat with Multiple PDFs 📚

A powerful Streamlit application that allows you to chat with multiple PDF documents using Google's Gemini Pro AI model. Upload your PDFs and ask questions to get instant, relevant answers from your documents.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red.svg)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_Pro-green.svg)

## ✨ Features

- 📄 Upload multiple PDF documents
- 💬 Interactive chat interface
- 🤖 Powered by Google's Gemini Pro AI
- 🔍 Intelligent document search
- 🎯 Precise answer extraction
- 🚀 Real-time responses
- 🎨 Beautiful user interface

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multiple-pdf-chatbot.git
cd multiple-pdf-chatbot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your Google API key:
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Create a `.env` file in the project root
   - Add your API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## 🚀 Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and go to `http://localhost:8501`

3. Use the application:
   - Click "Test API Connection" to verify your API key
   - Upload your PDF documents using the sidebar
   - Click "Process Documents" to analyze the PDFs
   - Start asking questions about your documents!

## 💡 Example Questions

- "What are the main points in the document?"
- "Can you summarize chapter 3?"
- "What does the document say about [specific topic]?"
- "Find all mentions of [keyword] in the documents."

## 🔧 Troubleshooting

- **API Key Issues**: Make sure your API key is correctly set in the `.env` file
- **PDF Processing Errors**: Ensure your PDFs are text-based and not scanned images
- **Model Errors**: Verify that you have enabled the Gemini API in your Google Cloud Console

## 🛡️ Dependencies

- streamlit==1.32.0
- PyPDF2==3.0.1
- google-generativeai==0.3.2
- python-dotenv==1.0.1

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

If you have any questions or suggestions, please open an issue in the repository.

---
Made with ❤️ using Streamlit and Google Gemini Pro
