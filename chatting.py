import openai

# Your API key
openai.api_key = "snk-proj-4WR8w3VjnCrr7ddnvGq35MdUAfm8esYrElXyPo5FlzM1SjlZzSYlhnzguWTEoE8Y4uUysJXA2KT3BlbkFJuQJAiPUDGg4g97xyXcNe9zlcRpApsGNwBF0s1tkf-9PJjta5rTnQafZMdt-L7QC1l3LyB4fiUA"

# Function to get response from ChatGPT
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Or use "gpt-3.5-turbo" for a less expensive model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# Get input from user
user_input = input("You: ")

# Get response from ChatGPT
response = chat_with_gpt(user_input)

print(f"ChatGPT: {response}")
