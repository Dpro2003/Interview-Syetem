# scoring.py
def calculate_score(answer):
    """
    Calculate the score based on the provided answer.
    :param answer: The transcribed answer provided by the user.
    :return: Score as an integer.
    """
    # Simple scoring logic: 5 points per word in the answer
    words = answer.split()
    score = len(words) * 5
    return score
