#Question 1 - Python Code
import openai

import os
from dotenv import load_dotenv

load_dotenv() 
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set your API key
client = openai.OpenAI(api_key=OpenAI_Key)

problem = input("Enter the problem statement: ")

messages = [
    {"role": "system", "content": "You generate a python code for the given problem, identify inputs needed as well and try to avoid pretext and post text."},
    {"role": "user", "content": f'Generate the python code for the problem:\n\n"{problem}"\n\nproblem: '}
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

code = response.choices[0].message.content.strip()
print(f"\n\ncode: {code}")