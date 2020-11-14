import tkinter as tk
from tkinter import ttk
from . import views

# main class application
class Application(tk.Tk):
    """Application root window"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Stock Screener")
        self.geometry("500x600")
        # make the whole app expandable horizontally
        self.columnconfigure(0, weight=1)
        # make the text window expandable
        self.rowconfigure(1, weight=1) 

        # row 0
        title = ttk.Label(self, text="JocoGum Stock Screener", font=("TkDefaultFont", "9"))
        title.grid(row=0, sticky="ns")
        # row 1
        self.screen = views.MyGuiScreener(self)
        self.screen.columnconfigure(0, weight=1)
        self.screen.rowconfigure(0, weight=1) 
        self.screen.grid(row=1, sticky="nsew")