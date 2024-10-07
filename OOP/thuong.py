from phuongthuc import TinhToan
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tooltip import ToolTip

class Thuong(TinhToan):
    def __init__(self, parent):
        super().__init__(parent, "Tính Thương")
        
        # Frame 1: Tính thương bình thường
        self.create_widgets()
        
        # Frame 2: Tính thương lấy dư
        self.frame2 = ttk.LabelFrame(self, text="Tính Thương lấy phần dư")
        self.frame2.grid(column=0, row=1, padx=8, pady=4)

        self.a2 = tk.StringVar()
        a_label2 = ttk.Label(self.frame2, text="a:")
        a_label2.grid(column=0, row=0)
        a2_entry = ttk.Entry(self.frame2, width=12,textvariable=self.a2)
        a2_entry.grid(column=1, row=0)
        
        self.b2 = tk.StringVar()
        b_label2 = ttk.Label(self.frame2, text="b:")
        b_label2.grid(column=0, row=1)
        b2_entry = ttk.Entry(self.frame2, width=12, textvariable=self.b2)
        b2_entry.grid(column=1, row=1)

        button_div_remainder = ttk.Button(self.frame2, text="Tính dư", command=self.calculate_remainder)
        button_div_remainder.grid(column=2, row=0)
        button_clear_2 = ttk.Button(self.frame2, text="Xóa", command=self.clear2)
        button_clear_2.grid(column=2, row=1)
        
        self.result2 = tk.StringVar()
        result_label2 = ttk.Label(self.frame2, text="Kết quả:")  # Thêm nhãn cho kết quả
        result_label2.grid(column=0, row=4)
        result2_entry = ttk.Entry(self.frame2, width=30, textvariable=self.result2, state="readonly")
        result2_entry.grid(column=1, row=4)

        # Frame 3: Tính thương lấy phần nguyên
        self.frame3 = ttk.LabelFrame(self, text="Tính Thương lấy phần nguyên")
        self.frame3.grid(column=0, row=2, padx=8, pady=4)

        self.a3 = tk.StringVar()
        a_label3 = ttk.Label(self.frame3, text="a:")
        a_label3.grid(column=0, row=0)
        a3_entry = ttk.Entry(self.frame3, width=12, textvariable=self.a3)
        a3_entry.grid(column=1, row=0)
        
        self.b3 = tk.StringVar()
        b_label3 = ttk.Label(self.frame3, text="b:")
        b_label3.grid(column=0, row=1)
        b3_entry = ttk.Entry(self.frame3, width=12, textvariable=self.b3)
        b3_entry.grid(column=1, row=1)

        button_div_integer = ttk.Button(self.frame3, text="Tính phần nguyên", command=self.calculate_integer)
        button_div_integer.grid(column=2, row=0)
        button_clear_3 = ttk.Button(self.frame3, text="Xóa", command=self.clear3)
        button_clear_3.grid(column=2, row=1)

        self.result3 = tk.StringVar()
        result_label3 = ttk.Label(self.frame3, text="Kết quả:")  # Thêm nhãn cho kết quả
        result_label3.grid(column=0, row=4)
        result3_entry = ttk.Entry(self.frame3, width=30, textvariable=self.result3, state="readonly")
        result3_entry.grid(column=1, row=4)
        ToolTip(a2_entry, "Nhập số a")
        ToolTip(b2_entry, "Nhập số b")
        ToolTip(button_div_remainder, "Tính dư")
        ToolTip(button_clear_2, "Xóa dữ liệu")
        ToolTip(result2_entry, "Kết quả tính toán")
        ToolTip(a3_entry, "Nhập số a")
        ToolTip(b3_entry, "Nhập số b")
        ToolTip(button_div_integer, "Tính phần nguyên")
        ToolTip(button_clear_3, "Xóa dữ liệu")
        ToolTip(result3_entry, "Kết quả tính toán")

    def calculate(self):
        # Hàm tính chia bình thường
        try:
            a_val = float(self.a.get())  
            b_val = float(self.b.get())  
            
            if b_val == 0:
                messagebox.showerror("Error", "Không thể chia cho 0")
                return

            result = a_val / b_val
            self.result.set(f"{a_val} / {b_val} = {result:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Tham số không hợp lệ")

    def calculate_remainder(self):
        # Hàm tính dư
        try:
            a_val = float(self.a2.get())
            b_val = float(self.b2.get())
            
            if b_val == 0:
                messagebox.showerror("Error", "Không thể chia cho 0")
                return

            x = a_val % b_val
            self.result2.set(f"{a_val} % {b_val} = {x:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Tham số không hợp lệ")

    def calculate_integer(self):
        # Hàm tính phần nguyên
        try:
            a_val = float(self.a3.get())
            b_val = float(self.b3.get())
            
            if b_val == 0:
                messagebox.showerror("Error", "Không thể chia cho 0")
                return

            x = a_val // b_val
            self.result3.set(f"{a_val} // {b_val} = {x:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Tham số không hợp lệ")
    def clear2(self):
            self.a2.set("")
            self.b2.set("")
            self.result2.set("")
    def clear3(self):
            self.a3.set("")
            self.b3.set("")
            self.result3.set("")
