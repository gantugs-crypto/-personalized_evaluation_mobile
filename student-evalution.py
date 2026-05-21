# Import necessary libraries
import os

# Function to create the quiz
def create_quiz():
    # Store the quiz questions, options, and answers
    questions = [
        {
            "question": "Choose the correct sentence:",
            "type": "multiple_choice",
            "options": [
                "A) She don't like apples.",
                "B) She doesn't likes apples.",
                "C) She doesn't like apples.",
                "D) She didn't liked apples."
            ],
            "answer": "C"
        },
        {
            "question": "Fill in the blank: He ____ to the market every Sunday.",
            "type": "short_answer",
            "answer": "goes"
        },
        {
            "question": "Identify the incorrect word: 'The boy run quickly to school.'",
            "type": "short_answer",
            "answer": "run"
        }
    ]
    return questions

# Function to conduct the quiz and collect answers
def conduct_quiz(questions):
    responses = []
    for q in questions:
        print(q["question"])  # Display the question
        if q["type"] == "multiple_choice":
            for option in q["options"]:  # Display multiple-choice options
                print(option)
            user_answer = input("Enter the option (A/B/C/D): ").strip().upper()
        elif q["type"] == "short_answer":
            user_answer = input("Your answer: ").strip().lower()
        responses.append({
            "question": q["question"],
            "correct_answer": q["answer"],
            "user_answer": user_answer
        })
    return responses

# Function to evaluate the quiz and provide personalized feedback
def evaluate_quiz(questions, responses):
    score = 0
    pros = []
    cons = []
    feedback = []

    # Evaluate each question
    for i, q in enumerate(questions):
        user_answer = responses[i]["user_answer"]
        correct_answer = q["answer"]

        # Check if the answer is correct
        if (q["type"] == "multiple_choice" and user_answer == correct_answer) or \
           (q["type"] == "short_answer" and user_answer == correct_answer.lower()):
            score += 1
            pros.append(f"Correct on question {i + 1}: {q['question']}")
        else:
            cons.append(f"Incorrect on question {i + 1}: {q['question']} - Correct answer: {correct_answer}")
    
    # Generate personalized feedback
    feedback.append(f"Bat scored {score}/{len(questions)}.")
    if score == len(questions):
        feedback.append("Excellent! You got all answers correct!")
    elif score > len(questions) // 2:
        feedback.append("Good job! You did well, but there's room for improvement.")
    else:
        feedback.append("Keep practicing! Review the notes on what went wrong to improve.")
    
    return score, pros, cons, feedback

# Function to generate the HTML file with results
def generate_html(responses, score, pros, cons, feedback):
    with open("Bat_quiz_results.html", "w") as file:
        # HTML structure
        file.write("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Bat's Quiz Results</title>
            <style>
                body {
                    font-family: 'Georgia', serif;
                    background-color: #1e1e1e;
                    color: #f5f5f5;
                    margin: 0;
                    padding: 0;
                }
                h1, h2 {
                    color: #00bfff;
                }
                .content {
                    padding: 20px;
                    max-width: 800px;
                    margin: auto;
                }
                .question {
                    margin-bottom: 20px;
                }
                .correct {
                    color: limegreen;
                }
                .incorrect {
                    color: red;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                table, th, td {
                    border: 1px solid #00bfff;
                }
                th, td {
                    padding: 10px;
                    text-align: left;
                }
                th {
                    background-color: #00bfff;
                    color: black;
                }
            </style>
        </head>
        <body>
            <div class="content">
                <h1>Bat's Quiz Results</h1>
                <h2>Quiz Questions and Answers</h2>
        """)

        # Write quiz questions, responses and if they were correct
        for i, r in enumerate(responses):
            correct_class = "correct" if r["user_answer"].lower() == r["correct_answer"].lower() else "incorrect"
            file.write(f"""
            <div class="question">
                <p><strong>Q{i + 1}:</strong> {r['question']}</p>
                <p>Your Answer: <span class="{correct_class}">{r['user_answer']}</span></p>
                <p>Correct Answer: {r['correct_answer']}</p>
            </div>
            """)

        # Write score
        file.write(f"<h2>Score: {score}/{len(responses)}</h2>")

        # Write pros and cons as a table
        file.write("""
        <h2>Pros and Cons</h2>
        <table>
            <tr>
                <th>Pros</th>
                <th>Cons</th>
            </tr>
            <tr>
                <td>
        """ + "<br>".join(pros) + "</td><td>" + "<br>".join(cons) + "</td></tr></table>")

        # Write personalized feedback
        file.write(f"""
        <h2>Personalized Feedback</h2>
        <p>{" ".join(feedback)}</p>
        </div>
        </body>
        </html>
        """)

# Main function to execute the quiz
def main():
    print("Welcome to Bat's English Quiz!")
    questions = create_quiz()  # Create the quiz
    responses = conduct_quiz(questions)  # Conduct the quiz
    score, pros, cons, feedback = evaluate_quiz(questions, responses)  # Evaluate the quiz
    generate_html(responses, score, pros, cons, feedback)  # Generate the HTML output
    print("Quiz complete! Results have been saved to 'Bat_quiz_results.html'.")

# Run the program
if __name__ == "__main__":
    main()