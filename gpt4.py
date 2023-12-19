#TEMPERATURE: 0 to 2. how creative it is. lower value=less creative, more deterministic
#MAX_TOKENS: inf. maximum number of tokens allowed for response (less=shorter response, cheaper).
#FREQUENCY PENALTY: -2 to 2. higher means supress repitition. Negative values = favour repitition. 0 is default.
#PRESENCE PENALTY: -2 to 2. higher value->penalise new words if they already appeared, i.e. increases likelihood of saying new topics
#TOP_P: 0 to 2. alt to temperature. lower means less creative.

import requests
import json

API_KEY = "YOUR_API_KEY_HERE"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

def generate_chat_completion(messages, model="gpt-4-1106-preview", temperature=1, max_tokens=None, frequency_penalty=0, presence_penalty=0, top_p=1):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty,
        "top_p": top_p,
        #"stream": True
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    print("gpt4 is generating response...")
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


#takes in the users input
user_input = []
print("your gpt4 prompt: ")
while True:
    try:
        line = input()
    except EOFError:
        break
    user_input.append(line)
concatenated_input = "\n".join(user_input)


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": concatenated_input}
]

response_text = generate_chat_completion(messages)
print("\ngpt4 response: ")
print(response_text)
