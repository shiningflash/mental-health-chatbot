import streamlit as st
from core.chatbot import generate_response

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
    # st.image("images/moon.png", width=100)
    # st.title("🌕 Moon")
    
    # Add a welcoming message
    st.subheader("🌟 Welcome!")
    st.write("Hi there! I'm Moon 🌙, your friend. I am always here to listen you. Let's talk about your day, your thoughts, or anything on your mind. ❤️")
    
    # Add a fun and engaging section to encourage interaction
    st.info("💬 Feeling sad or overwhelmed? Share your story with me — I'm here to brighten your day! ✨")
    
    # Clear conversation button
    st.markdown("")
    if st.button("Clear Our Conversation"):
        st.session_state.messages = [{"role": "assistant", "content": "Hi, I’m Moon 🌙, your friend. How can I brighten your day?"}]
        st.success("Conversation cleared! Let's start fresh.")

    # Add a lovely quote or tagline
    st.markdown("***")
    st.markdown(
        "🌕 **Moon: Always here for you.**",
        help="Moon is your empathetic friend, ready to chat and support you."
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
        st.write(response)

    # Add assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
