import streamlit as st
from core.chatbot import generate_response
from utils.helpers import get_base64_image

# Configure the Streamlit app
st.set_page_config(
    page_title="🌙 Moon - Your Friend",
    page_icon="🌕",
    layout="wide",
)

# Load external CSS for styling
with open("styles/chat_styles.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi, I’m Moon 🌙, your friend. How can I brighten your day?"}]

# Sidebar with warm information
with st.sidebar:
    st.image("images/moon.png", width=250)
    st.title('🌕 Moon')
    st.text("🌟A friend who\'s always here for you.\n💬 Let's talk about anything on your mind.\n❤️ I'm here to bring comfort and positivity to your day.")
    st.markdown("***")
    if st.button("🌀 Clear Our Conversation"):
        st.session_state.messages = [{"role": "assistant", "content": "Hi, I’m Moon 🌙, your friend. How can I brighten your day?"}]
    st.markdown("---")
    st.markdown(
        """
        <p class="sidebar-text">
        <b>🌕 Moon: Always here for you.</b><br>
        Made with ❤️ to brighten lives.
        </p>
        """,
        unsafe_allow_html=True,
    )

# Display chat history
st.markdown("### 💬 Let's Talk")

moon_image_base64 = get_base64_image("images/moon.png")

for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(
            f"""
            <div class="chat-message user">
                <img src="https://i.imgur.com/8Km9tLL.png" alt="User Icon" />
                <div class="content">{message['content']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="chat-message assistant">
                <img src="data:image/png;base64,{moon_image_base64}" alt="Moon Icon" />
                <div class="content">{message['content']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Input area
user_input = st.chat_input("What's on your mind? 🌟")
if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(
        f"""
        <div class="chat-message user">
            <img src="https://i.imgur.com/8Km9tLL.png" alt="User Icon" />
            <div class="content">{user_input}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Generate response
    with st.spinner("🌙 Thinking of something thoughtful..."):
        response = generate_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.markdown(
        f"""
        <div class="chat-message assistant">
            <img src="https://i.imgur.com/qkGNLFq.png" alt="Moon Icon" />
            <div class="content">{response}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
