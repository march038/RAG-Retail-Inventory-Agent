from apikey import apikey
import os
from langchain_experimental.agents import create_csv_agent
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
import streamlit as st


os.environ["OPENAI_API_KEY"] = apikey

agent= create_csv_agent(OpenAI(temperature=0),
                        "Inventarmanagement.CSV",
                        verbose=True)


# Streamlit Webapp erstellen
st.set_page_config(page_title="SAP Supermarkt Inventurassistent", page_icon="📃", layout="wide")
st.title('SAP Supermarkt Inventurassistent 📃')
question = st.text_input('Was möchtest du wissen?:', '')

# Initialisiere History im Session State, falls noch nicht geschehen, damit Chat History gespeichert wird
if 'QA_history' not in st.session_state:
    st.session_state.QA_history = []

# Antwort generieren und anzeigen
if question:
    response = agent.invoke(question)
    st.write(response['output'])

    # Zu History hinzufügen
    st.session_state.QA_history.insert(0,{'Frage':question,'Antwort': response['output']})

# Historie anzeigen
with st.expander('History'):
    for each in st.session_state.QA_history:
        # Formatiere und zeige jede Frage und Antwort aus der Historie an
        st.info(f"Frage: {each['Frage']}\nAntwort: {each['Antwort']}")

