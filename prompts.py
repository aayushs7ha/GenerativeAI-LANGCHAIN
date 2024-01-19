# Create your own use case as the name suggests 'Prompts'
# Custom use cases 
## Integrate our code with OpenAI
import os 
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st
os.environ['OPENAI_API_KEY'] = openai_key

# Streamlit framework
st.title('Celebrity Searches with OpenAPI')

input_text = st.text_input("Search the topic you want")

# create own custom prompts

pt = PromptTemplate(
    input_variable=['name'],
    template="Tell me about {name}"
)

# Initialize LLMchain
# Initialize openai llm to interact with the input
llm = OpenAI(temperature = 0.8)
chain=LLMChain(llm=llm,prompt=pt,verbose=True)
# Temp ranges from 0-1. How much balanced response you require, depends upon the temperature value you set 

if input_text:
    st.write(chain.run(input_text))