import tkinter as tk
from tkinter import ttk
from . import my_widgets as mw
from . import models
from . import jocogum_custom_filter


# my custom screener
class MyGuiScreener(tk.Frame):
    """My stock screener GUI"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        text_frame = tk.LabelFrame(self, text="Filtered Stocks", padx=5)
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)
        text_frame.grid(row=0, sticky="nsew")
        self.text_window = mw.MyScrolledText(text_frame)
        self.text_window.grid(row=0, sticky="nsew")
        # load the custom filter
        self.data = models.MySampleStockFilter()
        #self.data = jocogum_custom_filter.MyCustomStockFilter()
        

        button_show_stock = mw.MyButton(text_frame, text='Show Filtered Stocks')
        button_show_stock.config(command=self.print_watchlist)
        button_show_stock.grid(row=1, sticky="nsew")
        button_clear_screen = mw.MyButton(text_frame, text='Clear Screen')
        button_clear_screen.config(command=self.text_window.clear)
        button_clear_screen.grid(row=2, sticky="nsew")
    
    def print_watchlist(self):
        x = self.data.watchlist_no_of_trades
        sorted_list = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
        self.text_window.write("{0:^10s}|{1:^10s}|{2:^15s}|{3:^20s}".format("Stock", "Strategy", "No. of Trades", "Volume Filter"))
        for k,v in sorted_list.items():
            self.text_window.write("{0:^10s}|{1:^10s}|{2:^15.0f}|{3:^20s}".format(k, self.data.watchlist[k]["Strategy"], self.data.watchlist[k]["No. of Trades"], self.data.watchlist[k]["Volume Filter"]))
