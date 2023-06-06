import requests
import json

def send_chat_gpt_request(message):
    api_key = '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'
    url = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': message}
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()

    return response_json['choices'][0]['message']['content']

# Example usage
message = input('Enter your message: ')
response = send_chat_gpt_request(message)
print(response)
