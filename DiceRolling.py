import random
import tkinter as tk
from tkinter import messagebox

def roll_dice():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

def roll_button_clicked():
    dice_value = roll_dice()
    messagebox.showinfo("Dice Rolling Simulator", "You rolled: " + str(dice_value))

def exit_button_clicked():
    if messagebox.askokcancel("Dice Rolling Simulator", "Are you sure you want to exit?"):
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Dice Rolling Simulator")

# Create and configure the widgets
title_label = tk.Label(root, text="Dice Rolling Simulator", font=("Helvetica", 16))
title_label.pack(pady=20)

roll_button = tk.Button(root, text="Roll the Dice", font=("Helvetica", 14), command=roll_button_clicked)
roll_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Helvetica", 14), command=exit_button_clicked)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
