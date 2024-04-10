import streamlit as st
from PyPDF2 import PdfReader
import os
import google.generativeai as genai

# Configure Google Generative AI
os.environ['GOOGLE_API_KEY'] = 'AIzaSyA9gKlpwshtrWnCIQl2fKSid-aL1gvTxbk'
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize the Google Generative AI model
model = genai.GenerativeModel('gemini-1.0-pro-latest')

def get_pdf_text(pdf_docs):
    """Extract text from uploaded PDF files."""
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    return text

def ask_model(question, context):
    """Ask a question to the model, providing it the context extracted from the PDFs."""
    prompt = f"{context}\n\nQ: {question}\nA:"
    response = model.generate_content(prompt)
    return response.text

def display_conversation():
    """Displays the conversation history."""
    if "conversation" in st.session_state:
        for interaction in st.session_state.conversation:
            st.text_area("Question", value=interaction["question"], disabled=True, height=75)
            st.text_area("Answer", value=interaction["answer"], disabled=True, height=150)

def main():
    st.set_page_config("Document Conversation Bot", initial_sidebar_state="collapsed")
    st.header("Elicit")

    # Ensure 'conversation' and 'submitted' are initialized in session state at the start of main
    if "conversation" not in st.session_state:
        st.session_state.conversation = []
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    with st.sidebar:
        st.title("Settings")
        st.subheader("Upload Your Documents")
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True, type=['pdf'])
        if st.button("Process Documents"):
            with st.spinner("Extracting Text from Documents..."):
                raw_text = get_pdf_text(pdf_docs)
                st.session_state.document_text = raw_text
                st.success("Documents Processed. Ask me anything!")

    display_conversation()

    user_question = st.text_input("What do you want to elicit?", "", key="question_input")

    if st.button("Ask"):
        if user_question and 'document_text' in st.session_state:
            with st.spinner("Eliciting..."):
                answer = ask_model(user_question, st.session_state.document_text)
                st.session_state.conversation.append({"question": user_question, "answer": answer})
                st.session_state.submitted = not st.session_state.submitted  # Toggle to force widget refresh
        elif user_question:
            st.warning("Please upload and process documents first.")
        # Reset the input field by forcing a re-run
        st.experimental_rerun()

if __name__ == "__main__":
    main()
