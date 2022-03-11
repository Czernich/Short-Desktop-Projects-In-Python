from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class Gui():
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.current_score = 0
        self.score_label = Label(
            text=f"Score: {self.current_score}",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 20, "bold")
        )
        self.score_label.config(padx=20, pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=300,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.button_true = Button(text="", image=true_img, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=0, sticky="W")
        self.button_false = Button(text="", image=false_img, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=2, column=1, sticky="E")

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="No more questions.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



