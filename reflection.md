# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

The starter project was a Streamlit number-guessing game with an intentionally incomplete `logic_utils.py`. Running the supplied tests produced three `NotImplementedError` failures because the functions had not been refactored from `app.py` yet. The starter also changed the secret number to a string on alternating attempts, used a hard-coded range when starting a new game, and displayed hint text that contradicted the result.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Run `python -m pytest -q` | Existing logic tests run and report useful assertion results. | All three starter tests raised `NotImplementedError` from `logic_utils.py`. | `NotImplementedError: Refactor this function from app.py into logic_utils.py` |
| Guess `60` when secret is `50` on an even-numbered attempt | The result should be `Too High`. | The starter converted the secret to a string, which caused a type mismatch and could enter an invalid comparison path. | Type/comparison error or incorrect result, depending on the path. |
| Choose Hard, then start a new game | The secret should stay within the Hard range, `1` through `50`. | The starter displayed one range but generated the new secret with `random.randint(1, 100)`. | No console error; the state was inconsistent with the selected difficulty. |

## 2. How did you use AI as a teammate?

I used Hermes as an AI coding assistant to inspect the starter files, explain the relationship between Streamlit reruns and session state, identify the type inconsistency in `check_guess`, and propose a refactoring plan for `logic_utils.py`. One suggestion I accepted was to keep the game rules in pure functions and test them independently from the Streamlit interface; the six passing pytest tests verified that decision. I did not accept the idea of treating a decimal string as a valid whole-number guess because that could hide invalid input, so the repaired parser rejects decimals and returns a clear error.

## 3. Debugging and testing your fixes

I first ran the starter tests and recorded the expected `NotImplementedError` failures. After implementing the pure functions and updating the app to use them, I ran `python -m pytest -q`; all six tests passed. I also reviewed the repaired code to confirm that a secret remains an integer, that the selected difficulty controls both display and random-number generation, and that a new game resets its state together.

## 4. What did you learn about Streamlit and state?

Streamlit reruns the Python script from top to bottom whenever a user interacts with a widget. Ordinary local variables therefore do not persist between interactions. `st.session_state` provides the persistent state for the secret, attempts, score, status, and history, so those values must be initialized only when missing and reset together when a new game begins.

## 5. Looking ahead: your developer habits

I want to reuse the habit of reproducing a bug before changing code, then adding a focused test for the repaired behavior. I also want to ask AI for an explanation and a small plan before allowing it to edit multiple files, and then review the diff instead of assuming the suggestion is correct. This project reinforced that AI-generated code is a candidate implementation: human judgment, tests, and observed behavior are still required before treating it as reliable.
