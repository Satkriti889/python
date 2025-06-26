import tkinter as tk
from tkinter import messagebox
import joblib

# Load model and vectorizer
try:
    model = joblib.load("new_model_amazon_musical_instruments_reviews.pkl")
    vectorizer = joblib.load("new_amazon_musical_instruments_reviews.pkl")
except FileNotFoundError:
    messagebox.showerror("Error", "Model or vectorizer file not found. Train the model first.")
    raise

# GUI prediction function
def classify_review():
    review_text = entry.get("1.0", tk.END).strip()
    if review_text:
        review_vector = vectorizer.transform([review_text])
        prediction = model.predict(review_vector)[0]
        sentiment = "Negative 😠" if prediction in [1.0, 2.0] else "Neutral 😐" if prediction == 3.0 else "Positive 😊"
        result_label.config(text=f"Predicted Rating: {prediction}  ({sentiment})")
    else:
        messagebox.showwarning("Input Error", "Please enter a review.")

# Build GUI
root = tk.Tk()
root.title("Amazon Review Rating Predictor")
root.geometry("500x350")
root.configure(bg="#f4f4f4")

tk.Label(root, text="Amazon Review Classifier", font=("Helvetica", 16, "bold"), bg="#f4f4f4").pack(pady=10)

tk.Label(root, text="Enter a review text:", bg="#f4f4f4").pack()
entry = tk.Text(root, height=6, width=60)
entry.pack(pady=10)

tk.Button(root, text="Predict Rating", command=classify_review, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f4f4f4", fg="blue")
result_label.pack(pady=20)

root.mainloop()
