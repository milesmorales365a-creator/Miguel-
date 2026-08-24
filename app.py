from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Quiz questions (you can add more!)
QUIZ_QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "correct": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "correct": "4"
    },
    {
        "question": "What is the largest planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct": "Jupiter"
    },
    {
        "question": "Who wrote Romeo and Juliet?",
        "options": ["Jane Austen", "William Shakespeare", "Mark Twain", "Charles Dickens"],
        "correct": "William Shakespeare"
    },
    {
        "question": "What color is the sky on a clear day?",
        "options": ["Red", "Green", "Blue", "Yellow"],
        "correct": "Blue"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/quiz')
def get_quiz():
    # Shuffle questions and return them
    shuffled = random.sample(QUIZ_QUESTIONS, len(QUIZ_QUESTIONS))
    # Remove correct answers from being sent (we'll check on the server)
    quiz_data = []
    for q in shuffled:
        quiz_data.append({
            "question": q["question"],
            "options": q["options"]
        })
    return jsonify(quiz_data)

@app.route('/api/check-answer', methods=['POST'])
def check_answer():
    data = request.json
    question_index = data.get('question_index')
    selected_answer = data.get('answer')
    
    # Get the correct answer
    correct = QUIZ_QUESTIONS[question_index]['correct']
    
    # Check if correct
    is_correct = selected_answer == correct
    
    return jsonify({
        'correct': is_correct,
        'correct_answer': correct
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)