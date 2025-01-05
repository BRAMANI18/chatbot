import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz

# Load dataset
def load_dataset():
    try:
        dataset = pd.read_csv('studenthelpdeskDATASET.csv')
        dataset['Patterns'] = dataset['Patterns'].str.lower().str.strip()
        return dataset[['Intent', 'Patterns', 'Responses']].dropna()
    except FileNotFoundError:
        st.error("Dataset file 'studenthelpdeskDATASET.csv' not found.")
        return None

# Chatbot response logic
def chatbot_response(user_input, dataset):
    user_input = user_input.lower().strip()
    best_match = None
    highest_score = 0

    for _, row in dataset.iterrows():
        for pattern in row['Patterns'].split(','):
            score = fuzz.partial_ratio(user_input, pattern.strip())
            if score > highest_score:
                highest_score = score
                best_match = row['Responses']

    if highest_score > 50:
        return best_match
    else:
        # Suggest possible intents
        suggested_intents = dataset['Intent'].unique()[:3]  # Suggest top 3 intents
        suggestions = ", ".join(suggested_intents)
        return f"Sorry, I didn't understand that. Did you mean one of these: {suggestions}?"

# Main Streamlit App
st.title("Student Help Desk Chatbot")

dataset = load_dataset()
if dataset is not None:
    with st.expander("Dataset Preview"):
        st.dataframe(dataset)

if 'history' not in st.session_state:
    st.session_state.history = []

st.header("Chat with the Bot")
user_input = st.text_input("Enter your question:", "")

if st.button("Submit"):
    if not user_input.strip():
        st.warning("Please enter a valid question.")
    elif dataset is not None:
        response = chatbot_response(user_input, dataset)
        st.session_state.history.append(f"**You:** {user_input}")
        st.session_state.history.append(f"**Chatbot:** {response}")

    for message in st.session_state.history:
        st.write(message)
