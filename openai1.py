import openai

client = openai.OpenAI(api_key="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")

review = input("Enter your feedback: ")

messages = [
    {"role": "system", "content": "You classify restaurant feedback sentiment as Positive, Negative or Neutral"},
    {"role": "user", "content": f'Classify the sentiment of this review:\n\n"{review}"\n\nSentiment: '}
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

sentiment = response.choices[0].message.content.strip()
print(f"Sentiment: {sentiment}")