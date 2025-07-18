from tkinter import *
import random

# Game choices
choices = ['Rock', 'Paper', 'Scissors']

# Main window setup
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x450")
root.config(bg="#f9f9f9")

# Result display label
label_result = Label(root, text="", font=("Arial", 14), bg="#f9f9f9", fg="#333")
label_result.pack(pady=20)

# Labels to show choices
label_computer = Label(root, text="", font=("Arial", 12), bg="#f9f9f9", fg="gray")
label_computer.pack(pady=10)

label_player = Label(root, text="", font=("Arial", 12), bg="#f9f9f9", fg="gray")
label_player.pack(pady=10)

# Game logic function
def play_game(player_pick):
    comp_pick = random.choice(choices)

    label_player.config(text=f"You picked: {player_pick}")
    label_computer.config(text=f"Computer picked: {comp_pick}")

    if player_pick == comp_pick:
        outcome = "It's a draw!"
    elif (player_pick == 'Rock' and comp_pick == 'Scissors') or \
         (player_pick == 'Paper' and comp_pick == 'Rock') or \
         (player_pick == 'Scissors' and comp_pick == 'Paper'):
        outcome = "You win!"
    else:
        outcome = "Computer wins!"

    label_result.config(text=outcome)

# Button frame for game options
button_frame = Frame(root, bg="#f9f9f9")
button_frame.pack(pady=30)

# Game buttons
rock_button = Button(button_frame, text="🪨 Rock", width=12, height=2, font=("Arial", 12), command=lambda: play_game('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = Button(button_frame, text="📄 Paper", width=12, height=2, font=("Arial", 12), command=lambda: play_game('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = Button(button_frame, text="✂️ Scissors", width=12, height=2, font=("Arial", 12), command=lambda: play_game('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Exit game button
quit_button = Button(root, text="Exit", width=15, height=2, font=("Arial", 12), bg="red", fg="white", command=root.destroy)
quit_button.pack(pady=20)

# Run the app
root.mainloop()

