import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import webview

# Create TTKbootstrap window
root = ttk.Window(themename="darkly")
root.geometry("400x200")
root.title("Launcher")

def open_app():
    webview.create_window('How App', 'https://howapp.pythonanywhere.com/')
    webview.start()

btn = ttk.Button(root, text="Open Web App", bootstyle=SUCCESS, command=open_app)
btn.pack(pady=50)

root.mainloop()
