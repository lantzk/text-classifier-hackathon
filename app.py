import streamlit as st
from transformers import pipeline

# Set up the sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Set up the Streamlit app
st.title("Text Classification Bot")

# User input
user_input = st.text_area("Enter the text you want to classify:", height=100)

if st.button("Classify"):
    if user_input:
        # Perform classification
        result = classifier(user_input)[0]
        
        # Display results
        st.subheader("Classification Result:")
        st.write(f"Label: {result['label']}")
        st.write(f"Confidence: {result['score']:.4f}")
    else:
        st.warning("Please enter some text to classify.")

# Add some information about the model
st.sidebar.header("About")
st.sidebar.info("This is a simple text classification bot using a pre-trained sentiment analysis model. You can replace it with your own text classification model for different tasks.")