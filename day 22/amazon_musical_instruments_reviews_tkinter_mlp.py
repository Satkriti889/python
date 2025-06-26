import tkinter as tk
from tkinter import messagebox
import joblib

# Load trained model and vectorizer
model = joblib.load("model_amazon_musical_instruments_reviews.pkl")
vectorizer = joblib.load("amazon_musical_instruments_reviews.pkl")

# Function to predict rating
def classify_review():
    review_text = entry.get("1.0", tk.END).strip()
    if review_text:
        vec = vectorizer.transform([review_text])
        prediction = model.predict(vec)[0]
        result_label.config(text=f"Predicted Rating: {prediction}")
    else:
        messagebox.showwarning("Input Error", "Please enter a review.")

# Build GUI
root = tk.Tk()
root.title("Amazon Review Rating Classifier")
root.geometry("450x300")
root.config(bg="#e8f0fe")

tk.Label(root, text="Amazon Review Classifier", font=("Arial", 16), bg="#e8f0fe").pack(pady=10)

tk.Label(root, text="Enter your review:", bg="#e8f0fe").pack()
entry = tk.Text(root, height=6, width=50)
entry.pack(pady=5)

tk.Button(root, text="Predict Rating", command=classify_review, bg="#4CAF50", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#e8f0fe")
result_label.pack(pady=10)

root.mainloop()
