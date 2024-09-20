# scoring.py
def calculate_score(answer):

    words = answer.split()
    score = len(words) * 5
    return score
