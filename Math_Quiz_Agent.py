import random

class MathQuizAgent:
    def __init__(self, num_questions=5):
        self.num_questions = num_questions
        self.score = 0

    def generate_question(self):
        operation = random.choice(['+', '-', '*'])
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = eval(f"{num1} {operation} {num2}")
        return f"What is {num1} {operation} {num2}?", correct_answer

    def start_quiz(self):
        print("Welcome to the Math Quiz! Let's get started.\n")
        for _ in range(self.num_questions):
            question, correct_answer = self.generate_question()
            print(question)
            user_answer = input("Your answer: ")
            if int(user_answer) == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.\n")
        
        print(f"Quiz Over! Your score is {self.score}/{self.num_questions}.")

# Create an instance of the MathQuizAgent and start the quiz
agent = MathQuizAgent(num_questions=10)
agent.start_quiz()
