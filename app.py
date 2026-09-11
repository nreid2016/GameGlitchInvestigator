import random
import streamlit as st

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")
st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game, repaired and verified.")

st.sidebar.header("Settings")
difficulty = st.sidebar.selectbox("Difficulty", ["Easy", "Normal", "Hard"], index=1)
attempt_limit = {"Easy": 6, "Normal": 8, "Hard": 5}[difficulty]
low, high = get_range_for_difficulty(difficulty)
st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "difficulty" not in st.session_state or st.session_state.difficulty != difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []

st.subheader("Make a guess")
st.info(f"Guess a number between {low} and {high}. Attempts left: {attempt_limit - st.session_state.attempts}")

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input("Enter your guess:")
col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    ok, guess, error = parse_guess(raw_guess)
    if not ok:
        st.error(error)
    elif guess is None or not low <= guess <= high:
        st.error(f"Enter a whole number from {low} to {high}.")
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess)
        outcome = check_guess(guess, st.session_state.secret)
        messages = {"Win": "🎉 Correct!", "Too High": "📈 Too high — try a smaller number.", "Too Low": "📉 Too low — try a larger number."}
        if show_hint:
            st.warning(messages[outcome])
        st.session_state.score = update_score(st.session_state.score, outcome, st.session_state.attempts)
        if outcome == "Win":
            st.session_state.status = "won"
            st.balloons()
            st.success(f"You won! The secret was {st.session_state.secret}. Final score: {st.session_state.score}")
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.error(f"Out of attempts! The secret was {st.session_state.secret}. Score: {st.session_state.score}")

st.divider()
st.caption("Debugged with tests, human review, and AI assistance.")
