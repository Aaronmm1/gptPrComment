import requests
import os
cortex_token = os.getenv('GPT_TOKEN')  # DO NOT SHARE THIS OR COMMIT IT TO GIT!
use_case = 'Tim-Testing'  # Limited to 255 characters
api_version = '2024-02-01'
model_name = 'gpt-35-turbo-latest'

headers = {
    'accept': '*/*',
    'Authorization': f'Bearer {cortex_token}',
}

params = {
    'api-version': api_version,
}

json_data = {
    'messages': [
        {
            'content': 'Hello, please tell me a joke about insurance.',
            'role': 'user',
        },
    ],
    'use_case': use_case
}
def main():

    with open('code_diff.txt', 'r') as file:
        code_diff = file.read()

    response = requests.post()
    print(response.json()['choices'][0]['message']['content'])