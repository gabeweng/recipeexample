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

gangster_template = """Re-write the meals given below in the style of a New York mafia gangster:

Meals:
{meals}
"""

gangster_template = PromptTemplate(
    input_variables=['meals'],
    template=gangster_template
)

#chains

llm = OpenAI(openai_api_key=API_KEY, temperature=0.9)

meal_chain = LLMChain(
    llm=llm,
    prompt=meal_template,
    output_key="meals",  # the output from this chain will be called 'meals'
    verbose=True
)


gangster_chain = LLMChain(
    llm=llm,
    prompt=gangster_template,
    output_key="gangster_meals",  # the output from this chain will be called 'gangster_meals'
    verbose=True
)

overall_chain = SequentialChain(
    chains=[meal_chain, gangster_chain],
    input_variables=["ingredients"],
    output_variables=["meals", "gangster_meals"],
    verbose=True
)
