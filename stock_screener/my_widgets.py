import os
import tkinter
from tkinter import (messagebox, filedialog, ttk)

font_setting = ("TkDefaultFont", "9", "normal")


class MyButton(ttk.Button):
    def __init__(self, parent=None, **config):
        ttk.Button.__init__(self, parent, **config)
        ttk.Style().configure('my.TButton', padding=5, relief="flat",
                              background="blue", font=font_setting
                              )
        ttk.Style().map("my.TButton",
                        foreground=[('pressed', 'red'), ('active', 'blue')],
                        background=[('pressed', '!disabled', 'black'),
                                    ('active', 'white')]
                        )
        self.config(style="my.TButton")
        self.grid(sticky="nsew", padx=10, pady=10)


class MyEntry(ttk.Entry):
    def __init__(self, parent=None, **config):
        ttk.Entry.__init__(self, parent, **config)
        ttk.Style().configure("my.TEntry", padding=5, insertcolor="red",
                              insertbackground="red", selectforeground="white",
                              selectbackground="blue", font=font_setting
                              )
        ttk.Style().map("my.TEntry", foreground=[('focus', 'blue'),
                                                 ('!focus', 'black')])
        self.config(style="my.TEntry")
        self.grid(sticky="nsew", padx=10, pady=10)


class MyScrolledText(ttk.Frame):
    def __init__(self, parent=None, text='', height=0, width=0, **config):
        ttk.Frame.__init__(self, parent, borderwidth=1, relief="solid",
                           **config)
        self.grid(sticky="nsew", ipadx=10, ipady=10)
        sbar = ttk.Scrollbar(self)
        self.height = height
        self.width = width
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        text = tkinter.Text(self, relief="groove", insertbackground="red",
                            selectforeground="white", selectbackground="blue",
                            height=self.height, width=self.width
                            )
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)
        sbar.grid(row=0, column=1, sticky="nsew")
        text.grid(row=0, column=0, sticky="nsew")
        text.rowconfigure(0, weight=1)
        text.columnconfigure(0, weight=1)
        self.text = text

    def write(self, text):
        self.text.insert("end", str("\n"+text))
        self.text.see("end")
        self.text.update()

    def clear(self):
        self.text.delete("1.0", "end")
        self.text.update()


class MyLabel(tkinter.Label):
    def __init__(self, parent=None, **config):
        tkinter.Label.__init__(self, parent, **config)
        self.config(font=font_setting, relief="flat")
        self.grid(sticky="nsew")


class MyFrame(ttk.Frame):
    def __init__(self, parent=None, **config):
        ttk.Frame.__init__(self, parent, **config)
        self.grid(sticky="nsew", padx=10, pady=10)


class MyCombobox(ttk.Combobox):
    def __init__(self, parent=None, **config):
        ttk.Combobox.__init__(self, parent, **config)
        ttk.Style().configure("my.TCombobox", padding=5,
                              selectforeground="black",
                              )
        ttk.Style().map("my.TCombobox", foreground=[('!focus', 'black')])
        self.config(style="my.TCombobox", justify="center", font=font_setting, state="readonly")
        self.grid(sticky="nsew", padx=10, pady=10)


class MyProgressbar(ttk.Progressbar):
    def __init__(self, parent=None, **config):
        ttk.Progressbar.__init__(self, parent, **config)
        ttk.Style().configure("my.Horizontal.TProgressbar",
                              orient="horizontal",
                              length=300,
                              mode="indeterminate"
                              )
        ttk.Style().map("my.Horizontal.TProgressbar",
                        bordercolor=[('active', 'blue')],
                        background=[('active', 'black')]
                        )
        self.config(style="my.Horizontal.TProgressbar")
        self.grid(sticky="w", padx=5, pady=5)