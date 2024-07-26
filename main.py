import ttkbootstrap as ttk

from disappearing_text_app.ui import UI

root = ttk.Window(themename="lumen")
root.configure(width=1500, height=900)
ui = UI(root, width=100, height=50)
ui.place(x=0, y=0)
root.mainloop()
