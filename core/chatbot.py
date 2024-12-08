from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def generate_response(user_input: str) -> str:
    """
    Generate a response from OpenAI's Chat Completion model.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a friendly mental health assistant. Talk with humanistic tone. Give large response, with sweet word, proper empathy, and talk like friend, talk like home, no uncommon, unknown words. Use emoji as much as possible. Remember previous conversation."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"
