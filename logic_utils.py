"""Pure game rules for Game Glitch Investigator."""


def get_range_for_difficulty(difficulty: str):
    """Return the inclusive secret-number range for a difficulty."""
    ranges = {"Easy": (1, 20), "Normal": (1, 100), "Hard": (1, 50)}
    return ranges.get(difficulty, ranges["Normal"])


def parse_guess(raw: str):
    """Parse user input into ``(ok, integer_guess, error_message)``."""
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."
    try:
        value = int(raw.strip())
    except ValueError:
        return False, None, "That is not a whole number."
    return True, value, None


def check_guess(guess: int, secret: int):
    """Return ``Win``, ``Too High``, or ``Too Low`` for a guess."""
    if guess == secret:
        return "Win"
    return "Too High" if guess > secret else "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Apply the score rule for an outcome and attempt number."""
    if outcome == "Win":
        return current_score + max(10, 100 - 10 * attempt_number)
    if outcome == "Too High":
        return current_score + 5 if attempt_number % 2 == 0 else current_score - 5
    if outcome == "Too Low":
        return current_score - 5
    return current_score
