# 🎮 Game Glitch Investigator: The Impossible Guesser

## The Situation

This Streamlit app is a number-guessing game. The starter version intentionally contained bugs in state handling, comparison logic, user feedback, difficulty ranges, and score behavior. The repaired version separates the game rules into `logic_utils.py`, verifies them with pytest, and keeps the Streamlit layer focused on user interaction.

## Setup

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Run the automated tests with:

```bash
python -m pytest -q
```

## Bugs investigated and repaired

1. The starter's `logic_utils.py` contained `NotImplementedError` placeholders, so the supplied tests could not run.
2. The starter converted the secret number to a string on alternating attempts. That caused type errors and incorrect comparisons.
3. The starter displayed the range `1 to 100` even when the selected difficulty used a different range, and “New Game” always generated from `1` to `100`.
4. The starter's hint text said “Go HIGHER” after a guess was too high and “Go LOWER” after a guess was too low, which was opposite of what the player needed.
5. The starter initialized attempts at `1` and counted invalid guesses before validating them, producing confusing attempt counts.

## Repairs

- Implemented `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` in `logic_utils.py`.
- Kept the secret as an integer and compared integer values consistently.
- Used the selected difficulty range for both the UI and new secret numbers.
- Corrected hint wording and input validation.
- Reset secret, score, attempts, status, and history together when starting a new game.
- Added tests for winning, too-high, too-low, difficulty ranges, input parsing, and score floor behavior.

## Demo Walkthrough

For a reproducible example, choose **Normal** difficulty and use a debug secret of `50`:

1. Start the app with `python -m streamlit run app.py`.
2. Enter `40`; the game reports `Too Low` and the score changes by `-5`.
3. Enter `60`; the game reports `Too High` and the score changes according to the even-attempt score rule.
4. Enter `50`; the game reports `Win`, stops the game, and displays the final score.
5. Select **New Game**; the score, attempts, history, and secret reset for a new round.

## Test Results

The current automated test suite passes:

```text
6 passed in 0.00s
```

See `test_results.txt` for the captured command output.

## AI collaboration

AI was used as a debugging teammate to inspect the starter code, explain the state and comparison bugs, suggest a refactoring plan, and propose pytest coverage. Every change was reviewed against the source code and verified with the test suite. The final project should be reviewed by the student in their own environment before submission.
