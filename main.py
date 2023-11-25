import streamlit as st
from openai import OpenAI
import os

# Function to query GPT-4
def query_gpt4(prompt):

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=st.secrets['OPEN_AI_KEY']
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

# Streamlit app layout
st.title("GPT-4 Query App")

# Passcode implementation
passcode = st.sidebar.text_input("Enter the passcode:", type="password")

# Replace YOUR_PASSCODE with your chosen passcode
if passcode == "Hopper75":  
    st.success("Passcode Accepted")

    user_prompt = st.text_area("Enter your prompt for GPT-4:")

    if st.button("Submit"):
        with st.spinner('Querying GPT-4...'):
            gpt_response = query_gpt4(user_prompt)
            st.write(gpt_response)
else:
    st.error("Please enter a valid passcode in the sidebar to use this app.")
