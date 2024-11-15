import streamlit as st
import random

def main():
    st.title("Guess the Number Game")
    st.sidebar.title("Game Modes")
    
    mode = st.sidebar.radio("Select a Mode:", ("Machine Guesses", "User Guesses"))
    
    if mode == "Machine Guesses":
        machine_guess_mode()
    else:
        user_guess_mode()

def machine_guess_mode():
    st.header("Machine Guesses Your Number")
    st.write("Think of a number between 1 and 100 (inclusive). The machine will try to guess it.")
    
    if "low" not in st.session_state:
        st.session_state.low = 1
    if "high" not in st.session_state:
        st.session_state.high = 100
    if "guess" not in st.session_state:
        st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
    
    if "found" not in st.session_state:
        st.session_state.found = False

    if st.session_state.found:
        st.success(f"The machine guessed it! Your number is {st.session_state.guess}.")
        if st.button("Play Again"):
            reset_machine_guess_state()
    else:
        st.write(f"Machine's Guess: {st.session_state.guess}")
        user_response = st.radio("Is this your number?", ("Too Low", "Too High", "Correct"))

        if user_response == "Too Low":
            st.session_state.low = st.session_state.guess + 1
        elif user_response == "Too High":
            st.session_state.high = st.session_state.guess - 1
        elif user_response == "Correct":
            st.session_state.found = True

        if not st.session_state.found:
            st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
            st.experimental_rerun()

def reset_machine_guess_state():
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
    st.session_state.found = False

def user_guess_mode():
    st.header("You Guess the Machine's Number")
    st.write("Try to guess the number the machine has chosen between 1 and 100.")

    if "target_number" not in st.session_state:
        st.session_state.target_number = random.randint(1, 100)
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if user_guess < st.session_state.target_number:
            st.warning("Too Low! Try again.")
        elif user_guess > st.session_state.target_number:
            st.warning("Too High! Try again.")
        else:
            st.success(f"Congratulations! You guessed it in {st.session_state.attempts} attempts.")
            if st.button("Play Again"):
                reset_user_guess_state()

def reset_user_guess_state():
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0

if __name__ == "__main__":
    main()