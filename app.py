import streamlit as st
import google.generativeai as genai
from google.api_core.exceptions import InternalServerError
from dotenv import load_dotenv
import os

load_dotenv()

generation_config = {
    "temperature": 1,
    "top_p": 1,
    "max_output_tokens": 2048,
}

# TODO : support for other models
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)

st.title("Poem Generator")

title = st.text_area("Enter title for the poem: ", height=50)

num_lines = st.slider("Approx number of lines: ", 0, 50, value=10)

tone_options = [
    "Nostalgic",
    "Melancholic",
    "Joyful",
    "Other",
]
tone = st.selectbox("Select the tone or mood of the poem:", options=tone_options)

style_options = ["Free Verse", "Sonnet", "Haiku", "Other"]
style = st.radio("Style or form:", style_options)

prompt = f"Write a {style} poem titled {title} in approximately {num_lines} lines in {style} style or form"

if st.button("Generate Poem"):
    try:
        chat = model.start_chat()
        response = chat.send_message(prompt)
        st.code(response.text, line_numbers=False, language="text")
    except InternalServerError:
        st.write("An error occurred. Please try again.")