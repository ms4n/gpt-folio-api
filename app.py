import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPEN_API_KEY')

response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': 'what\'s the capital of India' }
    ],
    temperature=0,
    max_tokens=100
)

print(response)
