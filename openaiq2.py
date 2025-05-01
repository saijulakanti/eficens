#Question 2 - Translation
import openai

client = openai.OpenAI(api_key="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")

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