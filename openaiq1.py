import openai

client = openai.OpenAI(api_key=)

#integers = input("Input the integers as list: ")

messages = [
    {"role": "system", "content": "You generate a python code, to identify and output all pairs of numbers that sum up to a specified target number, from the given list of integers. The code should avoid duplicates and be efficientoptimized for efficiency. The inputs will be list of integers and target number. Give the code only no pretext or post text."}
    #{"role": "user", "content": f'Classify the sentiment of this review:\n\n"{review}"\n\nSentiment: '}
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

code = response.choices[0].message.content.strip()
print(f"code: {code}")