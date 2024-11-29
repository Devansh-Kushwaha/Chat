import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Replace with the desired model
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response.choices[0].text.strip()

while True:
    user_input = "Write a hello world program"
    if user_input.lower() == "quit":
        break
    response = chat_with_gpt(user_input)
    print("ChatGPT:", response)