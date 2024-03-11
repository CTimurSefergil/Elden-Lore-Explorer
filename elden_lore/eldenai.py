from openai import OpenAI
client = OpenAI()

completition = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "ToDo"},
        {"role": "user", "content": "ToDo"},
    ]
)

print(completition.choices[0].message)