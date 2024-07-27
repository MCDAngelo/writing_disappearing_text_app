import ttkbootstrap as ttk
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

from .timer import Timekeeper

TIMER_SEC = 5


class UI(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.parent = root
        self.grid(row=0, column=0)
        self.create_timer()
        self.create_input_textbox()
        self.create_save_button()
        self.parent.bind("<Key>", self.key_handler)
        self.textbox.bind("<FocusIn>", self.select_line)

    def create_timer(self):
        self.timer = Timekeeper(self, row=5, column=1, padx=0, pady=0)
        self.timer.new_timer(TIMER_SEC, font=("Courier", 42))

    def create_input_textbox(self):
        self.textbox = ttk.Text(
            self,
            width=100,
            height=25,
            wrap=tk.WORD,
            font=("TkDefaultFixed", 20),
        )
        self.textbox.insert(
            tk.END,
            "Get rid of your writer's block! Start typing, but don't stop, or you'll lose your progress 😈",
        )
        self.textbox.grid(row=2, column=0, columnspan=3, rowspan=3, pady=20, padx=40)

    def create_save_button(self):
        self.save_button = ttk.Button(
            self,
            text="Save Progress",
            command=self.save_text,
            bootstyle="primary",
        )
        self.save_button.grid(row=5, column=2, padx=0, pady=10)

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

    def select_line(self, event=None):
        self.textbox.tag_add("sel", "insert linestart", "insert lineend")
