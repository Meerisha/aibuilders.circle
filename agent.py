import os
from openai import OpenAI

# Make sure you set your API key in environment variables:
# export OPENAI_API_KEY="your_key_here"  (Mac)
# setx OPENAI_API_KEY "your_key_here"    (Windows)

client = OpenAI()

def run_agent(user_input: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("AI Agent is running. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent shutting down.")
            break

        reply = run_agent(user_input)
        print(f"\nAgent: {reply}\n")