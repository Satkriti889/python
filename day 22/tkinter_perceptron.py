import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import Perceptron
import tkinter as tk
from tkinter import messagebox

# Step 1: Load and preprocess data
df = pd.read_csv("SMSSpamCollection.unknown", sep='\t', header=None, names=['label', 'message'])
df['label'] = df['label'].map({'ham': 0, 'spam': 1})
x = df['message']
y = df['label']

# Step 2: Vectorize the text
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(x)

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

# Step 4: Train the Perceptron model
model = Perceptron()
model.fit(X_train, y_train)

# Step 5: Evaluate the model (optional for console)
y_pred = model.predict(X_test)
print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Step 6: Tkinter GUI
def classify_message():
    message = entry.get("1.0", tk.END).strip()
    if message:
        vectorized = vectorizer.transform([message])
        prediction = model.predict(vectorized)[0]
        result = "Spam " if prediction == 1 else "Ham "
        result_label.config(text=f"Prediction: {result}")
    else:
        messagebox.showwarning("Input Error", "Please enter a message to classify.")


# Create the main window
root = tk.Tk()
root.title("Spam Detector - Perceptron")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Widgets
title_label = tk.Label(root, text="SMS Spam Detector", font=("Helvetica", 16), bg="#f0f0f0")
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter your message:", bg="#f0f0f0")
entry_label.pack()

entry = tk.Text(root, height=5, width=40)
entry.pack(pady=5)

classify_button = tk.Button(root, text="Classify", command=classify_message, bg="#4CAF50", fg="white")
classify_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0")
result_label.pack(pady=20)

# Run the GUI loop
root.mainloop()
