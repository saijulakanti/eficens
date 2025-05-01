#Question 1 - Python Code
import openai

client = openai.OpenAI(api_key="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")

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