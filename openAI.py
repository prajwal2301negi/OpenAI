import os
import streamlit as st
from constants import openai_key

os.environ["OPENAI_API_KEY"] = openai_key

from langchain_community.llms import OpenAI 

# Streamlit framework
st.title("Langchain With OpenAI")

# Input text field
input_text = st.text_input("Search")

# Initialize OpenAI LLM
llm = OpenAI(temperature=0.8)  # range-> 0-1

# Process user input
if input_text:
    response = llm(input_text)  
    st.write(response)
