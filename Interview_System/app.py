from flask import Flask, render_template, request
from scoring import calculate_score
from proctoring import check_proctoring_compliance

app = Flask(__name__)


questions = [
    "What is your greatest strength?",
    "Where do you see yourself in five years?",
    "Why should we hire you?",
    "Describe a challenge you faced and how you overcame it."
]

@app.route('/')
def home():
    
    question = questions[0]
    return render_template('interview.html', question=question, question_number=0)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.form['answer']
    question_number = int(request.form['question_number'])

    
    #compliance = check_proctoring_compliance()
    

    score = calculate_score(answer)

    
    if question_number + 1 < len(questions):
        next_question = questions[question_number + 1]
        return render_template('interview.html', question=next_question, question_number=question_number + 1)

    
    return render_template('result.html', score=score, transcribed_answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
