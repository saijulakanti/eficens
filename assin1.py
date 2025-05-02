import openai

import os
from dotenv import load_dotenv

load_dotenv() 
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set your API key
client = openai.OpenAI(api_key=OpenAI_Key)

article = input("Provide the article: ")

messages1 = [
    {"role": "system", "content": "Summarize the given news article and mention the key details to be noted."},
    {"role": "user", "content": f'Summarize the given article:\n\n"{article}"\n\n'}
]

response1 = client.chat.completions.create(
    model="gpt-4o",
    messages=messages1,
    temperature=0
)

summary1 = response1.choices[0].message.content.strip()
print(f"\n\n\nSummary_1: {summary1}")

messages2 = [
    {"role": "system", "content": "Summarize the given news article and mention the key details to be noted."},
    {"role": "user", "content": f'Summarize the given article:\n\n"{article}"\n\n'}
]

response2 = client.chat.completions.create(
    model="gpt-4o",
    messages=messages2,
    temperature=0
)

summary2 = response2.choices[0].message.content.strip()
print(f"\n\n\nSummary_2: {summary2}")

messages3 = [
    {"role": "system", "content": "Summarize the given news article and provide the facts and a netral opinion on the article."},
    {"role": "user", "content": f'Summarize the given article:\n\n"{article}"\n\n'}
]

response3 = client.chat.completions.create(
    model="gpt-4o",
    messages=messages3,
    temperature=0
)

summary3 = response3.choices[0].message.content.strip()
print(f"\n\n\nSummary_3: {summary3}")