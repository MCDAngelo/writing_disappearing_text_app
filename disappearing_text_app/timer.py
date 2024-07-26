import tkinter as tk


class Timer(tk.Label):
    def __init__(self, parent, time, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.time = time
        self.running = False
        self.show_time()

    def show_time(self):
        self.config(text=str(self.time))

    def tick(self):
        if self.time > 0:
            self.time -= 1
        if self.time == 2:
            self.parent.configure(bootstyle="warning")
            self.parent.instructions.configure(bootstyle="inverse-warning")
            self.config(bg="#ff851b", fg="white")
        if self.time == 1:
            self.parent.configure(bootstyle="danger")
            self.parent.instructions.configure(bootstyle="inverse-danger")
            self.config(bg="#ff4136")
        if self.time <= 0:
            self.running = False
            self.parent.configure(bootstyle="default")
            self.parent.instructions.configure(bootstyle="default")
            self.config(bg="white", fg="#555555")
            self.parent.textbox.delete("1.0", tk.END)

        self.show_time()

    def start(self):
        self.parent.configure(bootstyle="default")
        self.running = True

    def stop(self):
        self.running = False


class Timekeeper:
    def __init__(self, frame, row, column, padx, pady):
        self.frame = frame
        self.row = row
        self.column = column
        self.padx = padx
        self.pady = pady

    def new_timer(self, time, **kwargs):
        self.timer = Timer(self.frame, time, **kwargs)
        self.timer.grid(
            row=self.row,
            column=self.column,
            padx=self.padx,
            pady=self.pady,
        )
        self.timer.start()
        self.tick()

    def tick(self):
        self.frame.after(1000, self.tick)
        if self.timer.running:
            self.timer.tick()
