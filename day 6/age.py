import streamlit as st

# Set a title for the app
st.title("Simple Streamlit App")

# Add a header
st.header("Greet the User")

# Get user's name using a text input widget
name = st.text_input("Enter your name:")

# Add a button
if st.button("Say Hello"):
    if name:
        st.success(f"Hello, {name}!")
    else:
        st.warning("Please enter your name.")

# Add a slider and show its value
age = st.text_input("Select your age:")
st.button("Show Age")
st.write(f"Your age is: {age}")
