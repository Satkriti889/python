# sentiment_app.py

import streamlit as st
import joblib

# ✅ Must be the first Streamlit call
st.set_page_config(page_title="Amazon Review Sentiment Classifier")

# Load model and vectorizer
@st.cache_resource
def load_model_and_vectorizer():
    try:
        model = joblib.load("new_model_amazon_musical_instruments_reviews.pkl")
        vectorizer = joblib.load("new_amazon_musical_instruments_reviews.pkl")
        return model, vectorizer
    except FileNotFoundError:
        st.error("❌ Model or vectorizer file not found. Please run the training script first.")
        return None, None

model, vectorizer = load_model_and_vectorizer()

# Page UI
st.title("🎸 Amazon Musical Instruments Review Sentiment Classifier")
st.markdown("Enter a review below and predict whether it's **Positive**, **Neutral**, or **Negative**.")

# Input box
user_input = st.text_area("📝 Write your review here", height=150)

# Predict button
if st.button("🔍 Predict Sentiment"):
    if model is not None and vectorizer is not None:
        if user_input.strip():
            try:
                vec = vectorizer.transform([user_input])  # ✅ Correct usage of vectorizer
                prediction = model.predict(vec)[0]        # ✅ Predict using model
                emoji = {
                    'Positive': '😊',
                    'Neutral': '😐',
                    'Negative': '😠'
                }
                st.success(f"**Sentiment:** {prediction} {emoji.get(prediction, '')}")
            except Exception as e:
                st.error(f"🚫 Prediction failed: {e}")
        else:
            st.warning("⚠️ Please enter some text above.")
