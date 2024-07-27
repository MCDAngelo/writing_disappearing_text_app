import ttkbootstrap as ttk

from disappearing_text_app.ui import UI

root = ttk.Window(themename="flatly")
root.configure(width=1500, height=900)
ui = UI(root, width=150, height=50, padding=20)
ui.place(x=0, y=0)
root.mainloop()
