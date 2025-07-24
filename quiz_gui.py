import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
from main import get_high_score, save_high_score, easy_questions, medium_questions, hard_questions

class QuizGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Quiz Game")
        self.root.geometry("600x400")
        self.root.configure(bg="#2C3E50")
        
        # Style configuration
        style = ttk.Style()
        style.configure("Custom.TButton", 
                       padding=10, 
                       font=("Arial", 12),
                       background="#3498DB")
        
        self.create_main_menu()
    
    def create_main_menu(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Title
        title = tk.Label(self.root, 
                        text="Quiz Game", 
                        font=("Arial", 24, "bold"),
                        bg="#2C3E50",
                        fg="white")
        title.pack(pady=30)
        
        # Buttons
        ttk.Button(self.root, 
                   text="Start Game",
                   command=self.start_game,
                   style="Custom.TButton").pack(pady=10)
        
        ttk.Button(self.root, 
                   text="View High Scores",
                   command=self.show_high_scores,
                   style="Custom.TButton").pack(pady=10)
        
        ttk.Button(self.root, 
                   text="Exit",
                   command=self.root.quit,
                   style="Custom.TButton").pack(pady=10)
    
    def start_game(self):
        # Difficulty selection window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        tk.Label(self.root, 
                text="Select Difficulty",
                font=("Arial", 20, "bold"),
                bg="#2C3E50",
                fg="white").pack(pady=30)
        
        difficulties = [("Easy", "easy"), ("Medium", "medium"), ("Hard", "hard")]
        for text, value in difficulties:
            ttk.Button(self.root,
                      text=text,
                      command=lambda v=value: self.start_quiz(v),
                      style="Custom.TButton").pack(pady=10)
    
    def start_quiz(self, difficulty):
        self.questions = {
            "easy": easy_questions,
            "medium": medium_questions,
            "hard": hard_questions
        }[difficulty]
        self.questions = random.sample(self.questions, len(self.questions))
        self.current_question = 0
        self.score = 0
        self.difficulty = difficulty
        self.start_time = time.time()
        self.show_question()
    
    def show_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            
            # Question
            tk.Label(self.root,
                    text=f"Question {self.current_question + 1}:",
                    font=("Arial", 16, "bold"),
                    bg="#2C3E50",
                    fg="white").pack(pady=10)
            
            tk.Label(self.root,
                    text=q["question"],
                    font=("Arial", 14),
                    bg="#2C3E50",
                    fg="white",
                    wraplength=500).pack(pady=10)
            
            # Answer buttons
            for option in q["options"]:
                ttk.Button(self.root,
                          text=option,
                          command=lambda o=option[0]: self.check_answer(o, q["answer"]),
                          style="Custom.TButton").pack(pady=5)
        else:
            self.show_results()
    
    def check_answer(self, selected, correct):
        if selected == correct:
            self.score += 1
            messagebox.showinfo("Correct! ✅", "Good job!")
        else:
            messagebox.showinfo("Wrong! ❌", f"The correct answer was {correct}")
        
        self.current_question += 1
        self.show_question()
    
    def show_results(self):
        elapsed_time = round(time.time() - self.start_time, 1)
        high_score = get_high_score(self.difficulty)
        
        if self.score > high_score:
            save_high_score(self.score, self.difficulty)
            message = f"🎉 New high score!\nScore: {self.score}/{len(self.questions)}\nTime: {elapsed_time} seconds"
        else:
            message = f"Score: {self.score}/{len(self.questions)}\nHigh Score: {high_score}\nTime: {elapsed_time} seconds"
        
        messagebox.showinfo("Quiz Finished!", message)
        self.create_main_menu()
    
    def show_high_scores(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        tk.Label(self.root,
                text="High Scores",
                font=("Arial", 20, "bold"),
                bg="#2C3E50",
                fg="white").pack(pady=20)
        
        for difficulty in ["easy", "medium", "hard"]:
            score = get_high_score(difficulty)
            tk.Label(self.root,
                    text=f"{difficulty.capitalize()}: {score}",
                    font=("Arial", 14),
                    bg="#2C3E50",
                    fg="white").pack(pady=10)
        
        ttk.Button(self.root,
                  text="Back to Menu",
                  command=self.create_main_menu,
                  style="Custom.TButton").pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameGUI(root)
    root.mainloop()