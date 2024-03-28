import openai

openai.api_key = " " 

print("ChatGPT: Hi, I'm ChatGPT. I'm a helpful assistant!")
messages = [
    {"role": "system", "content": "Hi ChatGPT, You are a helpful assistant!"},
]

try:
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat_completion["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
except:
    print("API KEY를 확인해주세요")
    exit()

while True:
    message = input("🤔: ")
    if message == "bye":
        break
    if message == "clear":
        print("\033[H\033[J")
        print("ChatGPT: Hi, I'm ChatGPT. I'm a helpful assistant")
        messages = [
            {"role": "system", "content": "Hi ChatGPT, You are a helpful assistant!"},
        ]
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat_completion["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        continue
        
    
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat_completion["choices"][0]["message"]["content"]
    print(f"🐱‍👤: {reply}")
    messages.append({"role": "assistant", "content": reply})