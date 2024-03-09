from openai import OpenAI
client = OpenAI()

userLanguage = input("Enter language: ")
userNeed = input("Enter need: ")

completition = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are very good at " + userLanguage + " and your goal is to write code and only code with this language"},
        {"role": "user", "content": userNeed},
    ]
)

print(completition.choices[0].message)