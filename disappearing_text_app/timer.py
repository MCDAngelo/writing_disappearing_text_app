import tkinter as tk


class Timer(tk.Label):
    def __init__(self, parent, time, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.original_time = time
        self.time = time
        self.running = False
        self.show_time()

    def show_time(self):
        self.config(text=str(self.time))

    def reset_formatting(self):
        self.parent.configure(bootstyle="default")
        self.parent.textbox.config(bg="white", fg="#555555")
        self.config(bg="white", fg="#555555")

    def tick(self):
        if self.time > 0 and self.running:
            self.time -= 1
        if self.time == 2:
            self.parent.configure(bootstyle="warning")
            self.parent.textbox.config(bg="#f39c12", fg="white")
            self.config(bg="#f39c12", fg="white")
        elif self.time == 1:
            self.parent.configure(bootstyle="danger")
            self.parent.textbox.config(bg="#e74c3c", fg="white")
            self.config(bg="#e74c3c", fg="white")
        elif self.time <= 0:
            self.running = False
            self.reset_formatting()
            self.parent.textbox.delete("1.0", tk.END)
            self.parent.timer.cancel_timer()
            self.restart(timer_ended=True)

        self.show_time()

    def start(self):
        self.parent.configure(bootstyle="default")
        self.running = True

    def stop(self):
        self.running = False

    def restart(self, timer_ended=False):
        self.stop()
        self.time = self.original_time + 1
        if timer_ended:
            self.time -= 1
        self.reset_formatting()


class Timekeeper:
    def __init__(self, frame, row, column, padx, pady):
        self.frame = frame
        self.row = row
        self.column = column
        self.padx = padx
        self.pady = pady
        self.job_id = None

    def new_timer(self, time, **kwargs):
        self.timer = Timer(self.frame, time, **kwargs)
        self.timer.grid(
            row=self.row,
            column=self.column,
            padx=self.padx,
            pady=self.pady,
        )

    def tick(self):
        self.job_id = self.frame.after(1000, self.tick)
        if self.timer.running:
            self.timer.tick()

    def cancel_timer(self):
        self.frame.after_cancel(self.job_id)
        self.timer.restart()
