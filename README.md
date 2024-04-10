# Elicit

Elicit is an advanced Generative AI  application based on Google's LLM designed to enable interactive conversations with your documents. By leveraging Google Generative AI, specifically the `gemini-1.0-pro-latest` model, Elicit transforms uploaded PDF documents into a rich source of conversational interaction. Users can effortlessly extract and comprehend complex information through a simple question-and-answer interface, making it easier than ever to navigate and understand the contents of their documents.

## Overview

Elicit revolutionizes the way we interact with document contents by providing a direct, conversational interface. This tool not only facilitates the extraction of information from PDFs but also enhances user engagement with textual content. Through the use of cutting-edge AI technology, Elicit ensures that users can engage with their documents in a more intuitive and efficient manner.

### Sample Demonstration Overview

![image](https://github.com/SatvikVarshney/Elicit/assets/114079530/27ff69ca-81d1-4afe-8180-1fe9b2f3c2e4)

This sample demonstration showcases a conversation with Elicit, based on information extracted from the PDF titled "Bridging The Divide." For those interested in exploring this interaction further, the sample PDF is available in the 'Sample PDFs' folder.


## Key Features

### Current Features:

- **PDF Document Upload**: Elicit supports the secure upload of PDF files, offering users the flexibility to handle multiple documents at once. This feature expands the contextual understanding of the AI, providing more accurate and relevant responses to queries.

- **Efficient Text Extraction**: Leveraging the PyPDF2 library, Elicit efficiently extracts text from uploaded PDFs. This ensures that the AI has access to all the readable content within the documents, laying the groundwork for informed conversational interactions.

- **Interactive AI Conversations**: At the core of Elicit is the ability to ask questions about the document's content and receive AI-generated responses. This conversational approach makes it easier for users to obtain the information they need without manually searching through documents.

### Planned Enhancements

- **Enhanced Chat-Bot Interface**: The aim is to enhance the user interface of the chat-bot, ensuring a seamless and intuitive experience that elevates interaction and engagement.

- **Advanced Data Extraction**: The current version supports text extraction from PDFs only. Future updates will expand capabilities to include extraction from images, tables, and graphics, significantly broadening the document processing range.

- **Inter-Document Processing Efficiency**: Improvements are targeted towards enhancing the efficiency of processing across multiple documents. Key priorities include optimizations in speed and memory, aiming for a robust and swift user experience.

- **Accessibility and Ease of Use**: Efforts are directed towards making the application more accessible, including enabling web access and simplifying the setup process. This includes removing the necessity for a unique Google API key for each user, making the tool more straightforward and user-friendly.


## How It Works

1. **Document Upload**: Users can upload their PDF documents directly through the Streamlit application interface. Elicit accepts multiple documents simultaneously, enriching the conversational context.

2. **Text Extraction**: Once uploaded, the documents are processed to extract text. This process is powered by the PyPDF2 library, ensuring accurate and comprehensive text extraction.

3. **Ask and Receive**: With the documents processed, users can then ask any question related to the content. Elicit, using Google Generative AI, generates context-aware responses, effectively conversing with the user based on the document's information.

## Technologies Used

- **Streamlit**: For building and deploying the application interface.
- **PyPDF2**: Utilized for the extraction of text from PDF documents.
- **Google Generative AI**: Powers the AI model responsible for generating conversational responses to user queries.

## Getting Started

### Installation
Clone the repository to get started:
```bash
git clone https://github.com/SatvikVarshney/Eicit.git
```

Navigate to the project directory:
```bash
cd Elicit
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```

To run Elicit on your local machine, clone the repository and ensure you have Streamlit, PyPDF2, and access to Google Generative AI configured with your API key. Use the following command to launch the application:

```bash
streamlit run Elicit_v_1.py
```


