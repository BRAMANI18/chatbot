import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz
import os
openai.api_key = os.getenv("OPENAI_API_KEY")


# Load dataset
def load_dataset():
    try:
        dataset = pd.read_csv('studenthelpdeskDATASET.csv')
        return dataset[['Intent', 'Patterns', 'Responses']].dropna()
    except FileNotFoundError:
        st.error("Dataset file 'studenthelpdeskDATASET.csv' not found.")
        return None

# Chatbot response logic
def chatbot_response(user_input, dataset):
    user_input = user_input.lower().strip()
    best_match = None
    highest_score = 0
    best_intent = None

    # Check for the best matching intent using fuzzy matching
    for _, row in dataset.iterrows():
        for pattern in row['Patterns'].split(','):
            score = fuzz.partial_ratio(user_input, pattern.lower().strip())
            if score > highest_score:
                highest_score = score
                best_match = row['Responses']
                best_intent = row['Intent']

    # Check if the highest score is above a threshold
    if highest_score > 50: 
        return best_match 
    else:
        return "Sorry, I didn't understand that. Can you please try asking in a different way?" 

# Main Streamlit App
st.title("Student Help Desk Chatbot")

# Load and display dataset (hidden for end-users)
dataset = load_dataset()
if dataset is not None:
    with st.expander("Dataset Preview"):
        st.dataframe(dataset)

# Session state for storing chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Input section
st.header("Chat with the Bot")
user_input = st.text_input("Enter your question:", "")

# Chatbot response
if st.button("Submit"):
    if not user_input.strip():
        st.warning("Please enter a valid question.")
    elif dataset is not None:
        response = chatbot_response(user_input, dataset)
        st.session_state.history.append(f"**You:** {user_input}")
        st.session_state.history.append(f"**Chatbot:** {response}")

    # Display chat history
    for message in st.session_state.history:
        st.write(message)
