import streamlit as st
import random

st.title("Rock,Paper,Scissor Game")

users_turn= st.selectbox("Move:", ["Rock", "Paper", "Scissors"])

if st.button("Play"):
    computer_turn=random.choice(["Rock","Paper","Scissor"])
    st.write(f"Computer chose: **{computer_turn}**")

    if users_turn ==computer_turn:
        st.info("Its Draw.")
    elif(users_turn=="Rock"and computer_turn=="Scissor") or (users_turn=="Paper"and computer_turn=="Rock")or(users_turn=="Scissor"and computer_turn=="Paper"):
        st.success("You win")
    else:
        st.error("You loose")