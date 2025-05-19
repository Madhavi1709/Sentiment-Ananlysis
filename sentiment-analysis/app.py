from textblob import TextBlob
import streamlit as st

st.set_page_config(page_title="Sentiment Analysis App")

st.title("Sentiment Analysis for a Comment")
st.subheader("Enter a comment below to analyze its sentiment:")

user_input = st.text_area("Your Comment")

if st.button("Analyze Sentiment"):
    if user_input:
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            st.success("Sentiment: Positive 😊")
        elif sentiment < 0:
            st.error("Sentiment: Negative 😠")
        else:
            st.info("Sentiment: Neutral 😐")
    else:
        st.warning("Please enter a comment to analyze.")
