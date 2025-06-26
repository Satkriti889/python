# sentiment_gui.py

import tkinter as tk
from tkinter import messagebox
import joblib

# Load model and vectorizer
try:
    model = joblib.load("new_model_amazon_musical_instruments_reviews.pkl")
    vectorizer = joblib.load("new_amazon_musical_instruments_reviews.pkl")
except FileNotFoundError:
    print("Model or vectorizer file not found. Run the training script first.")
    exit()

# Function to predict sentiment
def classify_input():
    review_text = entry.get("1.0", tk.END).strip()
    if review_text:
        vec = vectorizer.transform([review_text])
        prediction = model.predict(vec)[0]
        emoji = {
            'Positive': '😊',
            'Neutral': '😐',
            'Negative': '😠'
        }
        result_label.config(text=f"Sentiment: {prediction} {emoji.get(prediction, '')}")
    else:
        messagebox.showwarning("Input Error", "Please enter a review.")

# Build GUI
root = tk.Tk()
root.title("Amazon Review Sentiment Classifier")
root.geometry("500x350")
root.config(bg="#eef2f3")

tk.Label(root, text="Amazon Review Sentiment Classifier", font=("Arial", 16, "bold"), bg="#eef2f3").pack(pady=10)
tk.Label(root, text="Enter a review:", bg="#eef2f3").pack()

entry = tk.Text(root, height=6, width=60)
entry.pack(pady=10)

tk.Button(root, text="Predict Sentiment", command=classify_input, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#eef2f3", fg="blue")
result_label.pack(pady=20)

root.mainloop()
