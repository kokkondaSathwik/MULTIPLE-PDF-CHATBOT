
# Multiple PDF Chatbot 🤖

![Screenshot](https://github.com/kokkondaSathwik/MULTIPLE-PDF-CHATBOT/blob/main/intro.jpg?raw=true) <!-- Replace with actual image URL -->

---

## 🌍 Overview

The **Multiple PDF Chatbot 🤖** is an AI-powered application that allows users to **interact with one or more PDF documents** using natural language. It helps you **ask questions, extract insights, and summarize** content from complex or lengthy PDFs in real-time.

### ✨ Key Highlights
- 📂 **Upload and interact with multiple PDFs** at once  
- 💬 **Ask natural language questions** about your documents' content  
- 🧠 **Context-aware answers** powered by AI  
- 📄 **Generate summaries** of lengthy documents  
- 🖼️ **OCR support** for scanned/image-based PDFs  
- ⚡ **Fast and real-time responses** with LangChain & FAISS  
- 🖥️ **User-friendly Streamlit UI**

---

## 🔧 Tech Stack

| 🧩 **Layer**          | 🔧 **Tools & Libraries**                                                                 |
|-----------------------|------------------------------------------------------------------------------------------|
| 🎨 **Frontend**       | `Streamlit`                                                                              |
| 🧠 **Backend**        | `Python`                                                                                 |
| 📚 **Core Libraries** | `LangChain`, `PyPDF2`, `FAISS`, `OpenAI API`, `pytesseract` (OCR)                        |
| 🗂️ **Text Embedding** | `FAISS` for semantic similarity search                                                   |
| 📑 **PDF Handling**   | `PyPDF2` for parsing, `pytesseract` for OCR on scanned documents                         |

---

## 📊 Features

- ✅ **Upload and read multiple PDFs** simultaneously  
- ✅ **Ask questions** directly from the uploaded files  
- ✅ **Generate summaries** of lengthy documents  
- ✅ **OCR Support** for scanned PDFs (toggle option)  
- ✅ **Real-time responses** with context-based answers powered by OpenAI API

---

## 📱 How It Works

1. 📤 **Upload PDF files** (supports scanned and text PDFs)  
2. ❓ **Ask questions** like “Summarize chapter 4” or “What’s the definition of X?”  
3. 🔍 **LangChain** splits documents into chunks and indexes them with **FAISS**  
4. 🤖 The chatbot uses **OpenAI GPT** to generate an accurate, contextual response  
5. 💬 Responses are presented in a conversational interface for better readability  

---

## 🚫 Challenges & ✔️ Solutions

Challenge | Solution  
--- | ---  
Parsing large PDFs and scanned documents | Integrated PyPDF2 and optional OCR support with pytesseract  
Maintaining contextual accuracy in answers | Used FAISS for better similarity search and LangChain for context management  
Real-time performance with multiple files | Optimized embeddings and memory handling in LangChain  
Handling similar queries across documents | Added indexing per document to isolate results  

---

## 🚀 Future Enhancements

- 🔐 **User Login & Profiles** to save chat and document history  
- 🧠 **Long-term Memory** for ongoing conversation threads  
- 🌐 **Multilingual Support** for global users  
- 📝 **Highlight Source Text** in PDF viewer alongside answers  
- 📤 **Export Options** for summaries in PDF or CSV formats  
- 📊 **Analytics Dashboard** for document statistics and trends  

---

## 📄 Example Use Case

![Screenshot](https://github.com/kokkondaSathwik/MULTIPLE-PDF-CHATBOT/blob/main/result.jpg?raw=true) <!-- Replace with actual image URL -->

*Example Query:*  
**“What is Citizenship at the commencement of the Constitution?”**

**Bot Responds:**  
> "Pakistan shall be deemed to be a citizen of India at the commencement of this Constitution if..."

---

## 🚀 Get Started

```bash
git clone https://github.com/kokkondaSathwik/MULTIPLE-PDF-CHATBOT
cd MULTIPLE-PDF-CHATBOT
pip install -r requirements.txt
streamlit run app.py
```

---

## 📢 Contributions & Feedback

We welcome contributions, issues, and feature requests!  
- 🛠️ Create an Issue  
- 🔁 Fork and submit a Pull Request  
- 📧 Email: [sathwikkokkonda997@gmail.com](mailto:sathwikkokkonda997@gmail.com)

---

## 📄 License

Licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.

---

## 🙏 Acknowledgements

Special thanks to the open-source libraries and tools:  
**LangChain**, **OpenAI**, **FAISS**, **Streamlit**, **PyPDF2**, **pytesseract**, and all contributors who inspired this idea.
