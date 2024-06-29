import os
import streamlit as st
from google.generativeai import configure, GenerativeModel

# Set your API key as an environment variable
os.environ['GENAI_API_KEY'] = 'AIzaSyDzeATPLWRenJGapH8wOCtKEs_QFf6FPR0'  # Replace with your actual API key

# Configure the SDK with the API key
configure(api_key=os.getenv('GENAI_API_KEY'))

# Define generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the generative model
model = GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Streamlit app
st.title('Generative AI Chatbot')

# Function to interact with the generative model
@st.cache_resource
def start_chat():
    chat_session = model.start_chat(history=[])
    return chat_session

# Main interaction loop
chat_session = start_chat()

# User name input
user_name = st.text_input('Enter your name:', '')

if user_name:
    user_input = st.text_input('You:', '')

    if st.button('Send'):
        if user_input:
            # Prefix user input with their name
            user_message = f"{user_name}: {user_input}"
            response = chat_session.send_message(user_message)
            bot_response = response.text
            
            # Display user message and bot response
            # st.text_area('Conversation:', value=f"You: {user_input}\n\nBot: {bot_response}")
            st.write(f"**{user_name}:** {user_input}")
            st.write(f"**Bot:** {bot_response}")

    st.write('')

    # Display some information about the model and its capabilities
    st.write(f'Model Name: {model.model_name}')
else:
    st.write('Please enter your name to start the chat.')

