from apikey import apikey
import os
from langchain_experimental.agents import create_csv_agent
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
import streamlit as st

# set OpenAI API-key
os.environ["OPENAI_API_KEY"] = apikey

# create a Langchain CSV agent
agent= create_csv_agent(OpenAI(temperature=0.2),
                        "Inventarmanagement.CSV",
                        verbose=True)


# create a Streamlit webapp
st.set_page_config(page_title="SAP Supermarket Assistant", page_icon="📃", layout="wide")
st.title('SAP Supermarket Assistant 📃')
question = st.text_input('Hi, how can I help you?:', '')

# Initialize history in session state if not already done to save chat history
if 'QA_history' not in st.session_state:
    st.session_state.QA_history = []

# only if a question is entered call the agent and print the response's output part
if question:
    response = agent.invoke(question)
    st.write(response['output'])

    # as well as add the Q&A pair to the chast history
    st.session_state.QA_history.insert(0,{'Question':question,'Answer': response['output']})

# display the chat history
with st.expander('History'):
    for each in st.session_state.QA_history:
        # format and display every Q&A pair from the chat history
        st.info(f"Question: {each['Question']}\nAnswer: {each['Answer']}")

