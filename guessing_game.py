import streamlit as st
import random
def initialize_game():
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
if "target_number" not in st.session_state:
    initialize_game()
st.title("Guess the Number Game")
st.write("I have selected a number between 1 and 100. Can you guess it?")
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")
submit = st.button("Submit")
if submit:
    st.session_state.attempts += 1
    if guess == st.session_state.target_number:
        st.success(f"🎉 Congratulations! You guessed the number {st.session_state.target_number} in {st.session_state.attempts} attempts.")
        st.session_state.game_over = True
    elif guess < st.session_state.target_number:
        st.info("Try a higher number!")
    else:
        st.info("Try a lower number!")
if st.session_state.game_over:
    if st.button("Play Again"):
        initialize_game()