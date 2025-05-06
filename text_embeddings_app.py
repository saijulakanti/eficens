import openai
import os
from dotenv import load_dotenv

load_dotenv() 
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set your API key
client = openai.OpenAI(api_key=OpenAI_Key)

# Define the input text
input_text = input("Enter the input text: ")
# Call the embeddings endpoint
response = openai.embeddings.create(
    model="text-embedding-3-small",
    input=input_text,
    encoding_format="float"
)

# Print the embedding
embedding = response.data[0].embedding
print("Embedding vector:", embedding)
print(len(embedding))
