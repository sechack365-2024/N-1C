import os
from groq import Groq

# Create the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Set the system prompt
system_prompt = {
    "role": "system",
    "content": "あなたは便利なアシスタントです。私の言葉を繰り返した後に，かわいい決め台詞を追加してください．ただし出力はに鉤括弧は含めないでください．"
}

# Set the user prompt
user_input = input('入力してください: ')
while user_input != '':    
    user_prompt = {
        "role": "user", "content": user_input
    }

    # Initialize the chat history
    chat_history = [system_prompt, user_prompt]

    response = client.chat.completions.create(model="llama3-70b-8192",
                                                messages=chat_history,
                                                max_tokens=100,
                                                temperature=1.2)

    # Print the response
    print("Answer:", response.choices[0].message.content)
    user_input = input('入力してください: ')