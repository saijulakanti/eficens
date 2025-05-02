#Question 2 - Translation
import openai

import os
from dotenv import load_dotenv

load_dotenv() 
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set your API key
client = openai.OpenAI(api_key=OpenAI_Key)

#integers = input("Input the integers as list: ")

messages = [
    {"role": "system", "content": "You generate a paragraph describing the key features of an advanced renewable energy system in english. Then translate it from english to spanish. Ensure that the translation accurately conveys technical details and terminology used in the renewable energy sector. Mention a heading of the language as well."}
    #{"role": "user", "content": f'Classify the sentiment of this review:\n\n"{review}"\n\nSentiment: '}
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

paragraph = response.choices[0].message.content.strip()
print(f"paragraph:\n{paragraph}")