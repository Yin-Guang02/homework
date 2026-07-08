import random
import tkinter as tk
from tkinter import messagebox

def play_round(user_choice):
    """Handles the game logic when a user clicks a button."""
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    user_choice_label.config(text=f"Your Choice:\n{user_choice}")
    computer_choice_label.config(text=f"Computer Choice:\n{computer_choice}")
    
    if user_choice == computer_choice:
        result_text = "It's a Tie!"
        result_label.config(text=result_text, fg="orange")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_text = "You Win! 🎉"
        result_label.config(text=result_text, fg="green")
    else:
        result_text = "Computer Wins! 🤖"
        result_label.config(text=result_text, fg="red")


def reset_game():
    """Hint 5: Resets the game choices and results back to default."""
    user_choice_label.config(text="Your Choice:\n-")
    computer_choice_label.config(text="Computer Choice:\n-")
    result_label.config(text="Make your move!", fg="black")
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x350")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="Rock, Paper, Scissors Challenge", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=15)

choices_frame = tk.Frame(root, bg="#f0f0f0")
choices_frame.pack(pady=10)

user_choice_label = tk.Label(choices_frame, text="Your Choice:\n-", font=("Arial", 12), width=18, bg="white", relief="groove", bd=2, pady=10)
user_choice_label.pack(side=tk.LEFT, padx=15)

computer_choice_label = tk.Label(choices_frame, text="Computer Choice:\n-", font=("Arial", 12), width=18, bg="white", relief="groove", bd=2, pady=10)
computer_choice_label.pack(side=tk.RIGHT, padx=15)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 14, "bold"), bg="#f0f0f0", pady=10)
result_label.pack()

buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack(pady=10)

rock_btn = tk.Button(buttons_frame, text="✊ Rock", font=("Arial", 11, "bold"), width=10, bg="#ffcccb", command=lambda: play_round("Rock"))
rock_btn.pack(side=tk.LEFT, padx=5)

paper_btn = tk.Button(buttons_frame, text="✋ Paper", font=("Arial", 11, "bold"), width=10, bg="#ccffcc", command=lambda: play_round("Paper"))
paper_btn.pack(side=tk.LEFT, padx=5)

scissors_btn = tk.Button(buttons_frame, text="✌️ Scissors", font=("Arial", 11, "bold"), width=10, bg="#e0b0ff", command=lambda: play_round("Scissors"))
scissors_btn.pack(side=tk.LEFT, padx=5)

reset_btn = tk.Button(root, text="Reset Game 🔄", font=("Arial", 10), bg="#d3d3d3", command=reset_game)
reset_btn.pack(pady=15)

root.mainloop()