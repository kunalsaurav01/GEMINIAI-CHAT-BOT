from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Correcting getenv
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    response_text = "".join(chunk.text for chunk in response)
    return response_text

st.set_page_config(page_title="Q&A DEMO")

st.header("Your Chatbot 💬💬")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Capture input and submit button
input = st.text_input("Input your question:", key="input")
submit = st.button("Ask the question")

# Correcting append syntax
if submit and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("you", input, "bot", response))

st.subheader("Your Chatbox")

# Display chat history
for user_role, user_text, bot_role, bot_text in st.session_state['chat_history']:
    with st.container():
        st.markdown(f"""
            <div style="padding:10px; background-color:#f0f0f5; margin-bottom:10px; color:#000;">
                <strong>{user_role}</strong>: {user_text}
            </div>
            <div style="padding:10px; border-radius:10px; background-color:#e0f7fa; margin-bottom:10px; color:#000;">
                <strong>{bot_role}</strong>: {bot_text}
            </div>
        """, unsafe_allow_html=True)
