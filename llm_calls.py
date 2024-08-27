import openai, os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

def askGPT(prompt):

    client = openai.OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=1200,
        messages = [
            {'role':'user', 'content':prompt}
        ]
    )

    return response.choices[0].message.content

def askClaude(prompt):
    client = Anthropic(api_key=anthropic_api_key)
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=200,
        messages = [
            {'role':'user', 'content':prompt}
        ]
    )
    return response.content[0].text