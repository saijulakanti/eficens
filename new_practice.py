# pip install openai langchain tiktoken chromadb python-dotenv
import os
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
 
load_dotenv()  # Load environment variables from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")  # Get OpenAI API key from environment variable
 
loader = DirectoryLoader("./docs", glob="*.pdf", loader_cls=PyPDFLoader)  # Load PDF documents from the "docs" directory
documents = loader.load()  # Load the documents into memory
print(f"Total documents loaded: {len(documents)}")
 
spillter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)  # Initialize a text splitter to break documents into smaller chunks
texts = spillter.split_documents(documents)  # Split the loaded documents into smaller chunks
print(f"Total chunks created: {len(texts)}")  # Print the total number of chunks created
print("First chunk:", texts[0].page_content)
 
persistant_directory = "vector_db"
embedding = OpenAIEmbeddings()  
vectordb = Chroma.from_documents(documents=texts, embedding=embedding, persist_directory=persistant_directory)  # Create a vector database from the chunks
vectordb.persist()  
vectordb = None  
 
vectordb = Chroma(persist_directory=persistant_directory, embedding_function=embedding)  # Reload the vector database from the persisted directory
retrieval = vectordb.as_retriever(search_kwargs={"k": 2})
llm = OpenAI()
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retrieval, return_source_documents=True)  # Create a retrieval-based question-answering chain
 
 
print("🤖 Chatbot: Hello! Ask me anything from the PDFs. Type 'exit' to quit.")  # Greet the user and prompt for input
while True:
    query = input("Enter your query (or type 'exit' to quit): ")  # Prompt the user for a query
    if query.lower() in ['exit', 'quit']:  # Check if the user wants to exit
        print("Exiting...")
        break  # Exit the loop if the user types 'exit' or 'quit'
    response = qa_chain(query)  # Run the QA chain with the user's query
    print("Answer:", response["result"])  # Print the answer from the QA chain