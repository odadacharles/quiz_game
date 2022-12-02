class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def next_question(self):
        """
        Gets the correct question from the question list, prompts the user for an answer, and calls the
        'check_answer' method
        """
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. True or False?:").lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """
        Returns False until the user has answered all the questions in the list
        """
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        """
        checks if the user's answer to the question is correct
        """
        if user_answer == correct_answer.lower():
            print("You are correct!")
            self.score += 1
        else:
            print("Sorry, that's incorrect.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{len(self.questions_list)}")
        print("\n")
