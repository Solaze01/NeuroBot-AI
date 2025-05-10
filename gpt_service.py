import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def get_gpt_reply(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']
