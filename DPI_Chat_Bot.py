"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

def getGeminiResponse(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="A Better Chicago")
st.header("Check Grant Eligibility")

input = st.text_input("Input:",key="input")
submit = st.button("Check")
response = ""

if submit:
    response = getGeminiResponse(input)
    st.subheader("This is what we think...")
    st.write(response)
    


