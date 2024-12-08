from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"],
)

def generate_response(user_input: str) -> str:
    """
    Generate a response from OpenAI's Chat Completion model.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a friendly mental health assistant. Talk with humanistic tone. Give large response if needed, always with sweet word, so nice tone, proper empathy, and talk like friend, talk like home, no uncommon, unknown words. Use emoji as much as possible (avoid rainbow emoji). Remember previous conversation. Very positive, be realistic, and funny when you need. Be as nice as possible, with exciting and friendly tone."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"
