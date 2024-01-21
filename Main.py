from langchain.prompts import PromptTemplate
import streamlit as st

API_KEY = st.secrets["openai_api_key"]

#templates

meal_template = PromptTemplate(
    input_variables=["ingredients"],
    template="Give me an example of 2 meals that could be made using the following ingredients: {ingredients}",
)
