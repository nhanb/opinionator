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

    main = ttk.Frame(root, padding=5)

    posts_frame = ttk.Frame(main)
    posts_label = ttk.Label(posts_frame, text="Posts")
    posts = tk.StringVar(value=["It's not my fault that I'm not...", "Orange"])
    posts_listbox = tk.Listbox(posts_frame, listvariable=posts)

    content_frame = ttk.Frame(main)
    content_label = ttk.Label(content_frame, text="Content")
    content_text = tk.Text(content_frame)

    main.pack(fill=tk.BOTH, expand=True)
    posts_frame.pack(side=tk.LEFT, fill=tk.BOTH)
    posts_label.pack(anchor=tk.W)
    posts_listbox.pack(fill=tk.BOTH, expand=1)
    content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    content_label.pack(anchor=tk.W)
    content_text.pack(fill=tk.BOTH, expand=1)

    root.mainloop()
