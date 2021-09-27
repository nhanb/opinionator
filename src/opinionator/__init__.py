import importlib.resources
import sys
import tkinter as tk
from tkinter import Tk, ttk


def set_icon(root: Tk):
    with importlib.resources.path("opinionator.assets.haiku", "Misc_Scroll.png") as img:
        root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(file=img))


def main():
    root = Tk()
    root.title("Opinionator")
    root.geometry(sys.argv[1] if len(sys.argv) == 2 else "1000x600+100+100")
    set_icon(root)
    style = ttk.Style()
    style.theme_use("clam")

    frame = ttk.Frame(root, padding=5)
    frame.pack(fill=tk.BOTH, expand=True)
    pw = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)

    posts_frame = ttk.LabelFrame(pw, text="Posts")
    pw.add(posts_frame, weight=1)
    posts = tk.StringVar(value=["Nghe bảo tôi là con gái của vua", "Orange"])
    posts_listbox = tk.Listbox(posts_frame, listvariable=posts)
    posts_listbox.pack(fill=tk.BOTH, expand=True)

    content_frame = ttk.LabelFrame(pw, text="Content")
    pw.add(content_frame, weight=1)
    content_text = tk.Text(content_frame)
    content_text.pack(fill=tk.BOTH, expand=True)

    pw.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
