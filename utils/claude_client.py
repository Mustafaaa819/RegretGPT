import anthropic
from config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def ask_claude(prompt):
    response = client.messages.create(
        model = "claude-sonnet-4-6",
        max_tokens = 4000,
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.content[0].text