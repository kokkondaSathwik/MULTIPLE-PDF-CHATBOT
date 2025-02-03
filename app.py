import streamlit as st
from dotenv import load_dotenv










def main():

    load_dotenv()
    st.set_page_config(page_title="Chat with Multiple PDF", page_icon=":books:")
    st.header("Chat with Multiple PDF :books:")
    st.text_input("Ask a question related to your documents:")

    with st.sidebar:
        st.subheader("Upload your PDFs")
        st.file_uploader("Upload PDFs here and Click on 'Process'", type=['pdf'], accept_multiple_files=True)
        st.button("Process")

    












if __name__ == '__main__':
    main()