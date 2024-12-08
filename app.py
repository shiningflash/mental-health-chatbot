import time
import streamlit as st
from core.chatbot import generate_response

# Configure the Streamlit app
st.set_page_config(
    page_title="🌙 Moon - Your Friend",
    page_icon="🌕",
    layout="wide",
)

st.markdown(
    """
    <meta property="og:title" content="🌕 Moon - Your Friend" />
    <meta property="og:description" content="Moon: Always here for you. A friendly chatbot for your mental well-being." />
    <meta property="og:image" content="images/moon.png" />
    <meta property="og:url" content="https://moonishere.streamlit.app/" />
    """,
    unsafe_allow_html=True,
)

# Load external CSS for styling
with open("styles/chat_styles.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi, I’m Moon 🌙, your friend. How can I brighten your day?"}]

# Sidebar with warm and engaging information
with st.sidebar:
    # Moon's logo
    st.image("images/moon.png", width=200, caption="🌕 Moon: Always here for you.")
    
    # Welcoming section
    st.title("🌟 Welcome!")
    st.write(
        "Hi there! I'm **Moon 🌙**, your caring friend. "
        "I'm here to listen, support, and brighten your day. 💖 "
        "Let’s share your thoughts, feelings, or stories."
    )

    # Emotional support info
    st.info(
        """
        💬 Feeling sad, anxious, or overwhelmed?  
        🌟 Share your thoughts with me — I'm always here to listen.  
        🧘 Let’s work together to find comfort and positivity. ✨
        """
    )

    # Clear conversation button with feedback
    st.markdown("---")
    if st.button("🌀 Clear Our Conversation"):
        st.session_state.messages = [{"role": "assistant", "content": "Hi, I’m Moon 🌙, your friend. How can I brighten your day?"}]
        st.success("Conversation cleared! Let's start fresh. 🌈")
    

    # Footer with tagline
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; font-size: 14px; color: #777;">
        🌕 <b>Moon: Always here for you.</b> <br>
        Made with ❤️ to brighten lives.
        </div>
        """,
        unsafe_allow_html=True,
    )


# Display chat history using `st.chat_message`
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant", avatar="images/moon.png"):
            st.write(message["content"])

# Input area
user_input = st.chat_input("What's on your mind? 🌟")
if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    with st.chat_message("assistant", avatar="images/moon.png"):
        with st.spinner("🌙 Thinking of something thoughtful..."):
            response = generate_response(user_input)
        
        # Gradually display response
        placeholder = st.empty()  # Create a placeholder
        displayed_text = ""
        for char in response:
            displayed_text += char
            placeholder.markdown(displayed_text)  # Update the placeholder content
            time.sleep(0.01)  # Adjust typing speed (0.01 seconds per character)

    # Add assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
