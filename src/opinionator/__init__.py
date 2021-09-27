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
    root.geometry(sys.argv[1] if len(sys.argv) == 2 else "800x600+100+100")
    set_icon(root)
    style = ttk.Style()
    style.theme_use("clam")

    frame = ttk.Frame(root, padding=5)
    frame.pack(fill=tk.BOTH, expand=True)
    pw = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)

    left = ttk.LabelFrame(pw, text="One", width=150)
    pw.add(left)

    right = ttk.LabelFrame(pw, text="Two")
    pw.add(right)

    pw.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
