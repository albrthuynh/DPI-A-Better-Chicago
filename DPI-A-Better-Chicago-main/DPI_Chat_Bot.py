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
    {
        'role': 'user',
        'parts': ['You are a specialist at determining grant eligibility for A-Better-Chicago, a project hosted by DPI.']
    },
    {
        'role': 'model',
        'parts': ['Sure.'],
    },
  ]
)


# resp = chat_session.send_message(
#     content='Does McDonalds quality for a grant according to the project a-better-chicago',
# )

# p
# rint(resp.text)

response = model.generate_content([
  "input: McDonald's",
  "output: This is not aligned with A-Better-Chicago's values. Please provide a non-profit organization. This is not aligned because they do not support health and wellness initiatives",
  "input: Burger King",
  "output: This is not aligned with A-Better-Chicago's values. Please provide a non-profit organization. This is not aligned because they do not support health and wellness initiaitves",
  "input: Wendy's",
  "output: This is not aligned with A-Better-Chicago's values. Please provide a non-profit organization. This is not aligned because they do not support health and wellness initiaitves",
  "input: Culvers",
  "output: This is not aligned with A-Better-Chicago's values. Please provide a non-profit organization. This is not aligned because they do not support health and wellness initiaitves",
  "input: In and Out",
  "output: This aligns with A-Better-Chicago values! This organization helps with providing students.",
  "input: Dominos",
  "output: This aligns with A-Better-Chicago values! This company donates to the partner's foundation which helps employees facing hardships like natural disasters or injuries.",
  "input: A House in Austin",
  "output: This organization aligns with A-Better-Chicago values!",
  "input: Dream on Education",
  "output: This organization aligns with A-Better-Chicago values!",
  "input: Digital Scholars",
  "output: This organization aligns with A-Better-Chicago values!",
  "input: Everyone Can Code",
  "output: This organization aligns with A-Better-Chicago values!",
  "input: Chicago Lighthouse Mission and Activities",
  "output: This organization is a 990 organization that aligns with A-Better-Chicago values because its mission is to provide education and youth development, provides vocational and employment services, and enable comprehensive support services",
  "input: Carole Robertson Center",
  "output: This organization is a 990 organization and aligns with A-Better-Chicago values because it provides education, family and community support, and provides high-impact programs",
  "input: Chicago HOPES for Kids",
  "output: This organization is a 990 organization and aligns with A-Better-Chicago values because it focuses on education, supports vulnerable populations, and has a community impact",
  "input: College Board",
  "output: This organization is a non-profit organization but does not align with A-Better-Chicago's values because it does not align with opportunities for low-income Black and Latinx Youth nor support Chicago’s high-impact nonprofits.",
])



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
else:
    response = getGeminiResponse("Give a response that states to the user to give a company that they think could qualify for a grant")
    st.subheader("Give a Company That Could Qualify for a Grant")
    st.write(response)