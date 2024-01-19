## Integrate our code with OpenAI
import os 
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st
os.environ['OPENAI_API_KEY'] = openai_key

# Streamlit framework
st.title('Langchain Demo with OpenAPI')

input_text = st.text_input("Search the topic you want")

# Initialize openai llm to interact with the input
llm = OpenAI(temperature = 0.8)
# Temp ranges from 0-1. How much balanced response you require, depends upon the temperature value you set 

if input_text:
    st.write(llm(input_text))
