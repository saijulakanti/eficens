import openai

import os
from dotenv import load_dotenv

load_dotenv() 
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set your API key
client = openai.OpenAI(api_key=OpenAI_Key)

jd = input("Provide the job description: ")

resume = input("Provide the resume: ")

messages = [
    {"role": "system", "content": "You will act like a hiring manager, compare the resume with the job description. If resume is suitable for job description, give the highlights of the resume which are suitable for the job role."},
    {"role": "user", "content": f'Evaluate the given resume with job description\n\nJob Description: "{jd}"\n\nResume:\n{resume}'}
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

evaluation = response.choices[0].message.content.strip()
print(f"\n\n\nEvaluation: {evaluation}")