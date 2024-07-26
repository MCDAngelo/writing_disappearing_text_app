import ttkbootstrap as ttk
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

from .timer import Timekeeper

TIMER_SEC = 5


class UI(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.parent = root
        self.create_timer()
        self.create_instructions_info()
        self.create_input_textbox()
        self.create_save_button()
        self.parent.bind("<Key>", self.key_handler)

    def create_instructions_info(self):
        self.instructions = ttk.Label(
            self,
            width=120,
            font=("Courier", 16),
            text="Break that writer's block! Start typing, but don't stop, or you'll lose your progress 😈",
        )
        self.instructions.grid(row=0, column=1, columnspan=3, pady=10)

    def create_timer(self):
        self.timer = Timekeeper(self, row=0, column=0, padx=40, pady=20)
        self.timer.new_timer(TIMER_SEC, font=("Courier", 42))

    def create_input_textbox(self):
        self.textbox = ttk.Text(
            self,
            width=120,
            height=20,
            wrap=tk.WORD,
            font=("Helvetica", 16),
        )
        self.textbox.insert(tk.END, "Start typing here ... ")
        self.textbox.grid(row=1, column=1, columnspan=3, pady=10)

    def create_save_button(self):
        self.save_button = ttk.Button(
            self,
            text="Save Progress",
            command=self.save_text,
            bootstyle="success",
        )
        self.save_button.grid(row=2, column=4, padx=20, pady=20)

    def save_text(self):
        entered_text = self.textbox.get("1.0", tk.END)
        filename = asksaveasfilename()
        with open(filename, mode="w") as f:
            f.write(entered_text)

    def key_handler(self, event):
        if self.timer.job_id is not None:
            self.timer.cancel_timer()
        self.timer.timer.start()
        self.timer.tick()
