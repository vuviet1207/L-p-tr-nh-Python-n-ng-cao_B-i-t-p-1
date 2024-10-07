import tkinter as tk
from tkinter import ttk
from tooltip import ToolTip
class TinhToan(ttk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.title = title
        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.LabelFrame(self, text=self.title)
        self.frame.grid(column=0, row=0, padx=8, pady=4)

        a_label = ttk.Label(self.frame, text="a:")
        a_label.grid(column=0, row=0)
        self.a = tk.StringVar()
        a_entry = ttk.Entry(self.frame, width=12, textvariable=self.a)
        a_entry.grid(column=1, row=0)
        a_entry.focus()  

        b_label = ttk.Label(self.frame, text="b:")
        b_label.grid(column=0, row=1)
        self.b = tk.StringVar()
        b_entry = ttk.Entry(self.frame, width=12, textvariable=self.b)
        b_entry.grid(column=1, row=1)

        button1 = ttk.Button(self.frame, text="Tính", command=self.calculate)
        button1.grid(column=3, row=0)
        button2 = ttk.Button(self.frame, text="Xóa", command=self.clear)
        button2.grid(column=3, row=1)


        self.result = tk.StringVar()
        result_label = ttk.Label(self.frame, text="Kết quả:")  # Thêm nhãn cho kết quả
        result_label.grid(column=0, row=4)
        result_entry = ttk.Entry(self.frame, width=30, textvariable=self.result, state="readonly")
        result_entry.grid(column=1, row=4)
        ToolTip(a_entry, "Nhập số a")
        ToolTip(b_entry, "Nhập số b")
        ToolTip(button1, "Tính toán")
        ToolTip(button2, "Xóa dữ liệu")
        ToolTip(result_entry, "Kết quả tính toán")
    
    def calculate(self):
        raise NotImplementedError("Chưa có phương thức tính toán")
    
    def clear(self):
        self.a.set("")
        self.b.set("")
        self.result.set("")
