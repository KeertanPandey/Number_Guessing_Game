import tkinter as tk
from tkinter import messagebox

from gamelogic import generate_sec_num, check_guess
from Score import calculate_score


class GuessingGameGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Secret Number")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.secret_number = generate_sec_num()
        self.attempts = 0
        self.max_attempts = 7

        # -------------------------
        # Title
        # -------------------------
        self.title_label = tk.Label(
            root,
            text="🎮 Guess the Secret Number",
            font=("Arial", 22, "bold")
        )
        self.title_label.pack(pady=20)

        # -------------------------
        # Instructions
        # -------------------------
        self.info_label = tk.Label(
            root,
            text="I have selected a number between 1 and 100.\n"
                 "You have 7 attempts.",
            font=("Arial", 13)
        )
        self.info_label.pack(pady=10)

        # -------------------------
        # Guess Label
        # -------------------------
        self.guess_label = tk.Label(
            root,
            text="Enter your guess:",
            font=("Arial", 14)
        )
        self.guess_label.pack(pady=10)

        # -------------------------
        # Guess Entry
        # -------------------------
        self.guess_entry = tk.Entry(
            root,
            font=("Arial", 18),
            justify="center",
            width=10
        )
        self.guess_entry.pack(pady=5)

        # -------------------------
        # Guess Button
        # -------------------------
        self.guess_button = tk.Button(
            root,
            text="Guess",
            font=("Arial", 14, "bold"),
            width=12,
            command=self.check_player_guess
        )
        self.guess_button.pack(pady=15)

        # -------------------------
        # Result
        # -------------------------
        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 18, "bold")
        )
        self.result_label.pack(pady=10)

        # -------------------------
        # Attempts
        # -------------------------
        self.attempts_label = tk.Label(
            root,
            text="Attempts remaining: 7",
            font=("Arial", 13)
        )
        self.attempts_label.pack(pady=10)

        # -------------------------
        # New Game Button
        # -------------------------
        self.new_game_button = tk.Button(
            root,
            text="New Game",
            font=("Arial", 13),
            width=12,
            command=self.new_game
        )
        self.new_game_button.pack(pady=15)

    # =================================
    # Check Player Guess
    # =================================

    def check_player_guess(self):

        try:
            guess = int(self.guess_entry.get())

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number."
            )
            return

        # Check range
        if guess < 1 or guess > 100:
            messagebox.showwarning(
                "Invalid Number",
                "Please enter a number between 1 and 100."
            )
            return

        # Increase attempts
        self.attempts += 1

        # Check guess using game_logic module
        result = check_guess(guess, self.secret_number)

        self.result_label.config(text=result)

        # Correct answer
        if result == "Correct!":

            player_score = calculate_score(self.attempts)

            self.attempts_label.config(
                text=f"Attempts used: {self.attempts}"
            )

            messagebox.showinfo(
                "🎉 Congratulations!",
                f"You guessed the number correctly!\n\n"
                f"Attempts: {self.attempts}\n"
                f"Score: {player_score}"
            )

            self.guess_button.config(state="disabled")

            return

        # Incorrect answer
        attempts_remaining = self.max_attempts - self.attempts

        self.attempts_label.config(
            text=f"Attempts remaining: {attempts_remaining}"
        )

        # Game Over
        if self.attempts == self.max_attempts:

            messagebox.showerror(
                "Game Over!",
                f"You used all 7 attempts.\n\n"
                f"The secret number was: {self.secret_number}"
            )

            self.guess_button.config(state="disabled")


    # =================================
    # New Game
    # =================================

    def new_game(self):

        self.secret_number = generate_sec_num()
        self.attempts = 0

        self.guess_entry.delete(0, tk.END)

        self.result_label.config(text="")

        self.attempts_label.config(
            text="Attempts remaining: 7"
        )

        self.guess_button.config(state="normal")

        self.guess_entry.focus()


# =====================================
# Start Application
# =====================================

root = tk.Tk()

game = GuessingGameGUI(root)

root.mainloop()