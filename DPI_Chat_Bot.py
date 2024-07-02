"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import pathlib
import textwrap
import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown

genai.configure(api_key='AIzaSyAcd_8ZR9O9IA0XJWGMBpVTg87RI9kmXmA')

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



userResponse = ""

while userResponse != "stop":
    userResponse = input("What is the name of your organization and what is their data?\nSay stop to end the conversation\n\n")
    response = chat_session.send_message(userResponse)
    print(response.text)

print("GOODBYE!")




