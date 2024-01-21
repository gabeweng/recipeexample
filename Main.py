from langchain.prompts import PromptTemplate
import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

API_KEY = st.secrets["openai_api_key"]

#templates

meal_template = PromptTemplate(
    input_variables=["ingredients"],
    template="Give me an example of 2 meals that could be made using the following ingredients: {ingredients}",
)

#chains

llm = OpenAI(openai_api_key=API_KEY, temperature=0.9)

meal_chain = LLMChain(
    llm=llm,
    prompt=meal_template,
    output_key="meals",  # the output from this chain will be called 'meals'
    verbose=True
)
