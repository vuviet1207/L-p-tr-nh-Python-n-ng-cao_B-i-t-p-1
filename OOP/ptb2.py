from phuongthuc import TinhToan
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import math
from tooltip import ToolTip

class PTb2(TinhToan):
    def __init__(self, parent):
        super().__init__(parent, "Giải phương trình bậc 2 ax^2 + bx + c = 0")
        c_label = ttk.Label(self.frame, text="c:")
        c_label.grid(column=0, row=3)
        self.c = tk.StringVar()
        c_entry = ttk.Entry(self.frame, width=12, textvariable=self.c)
        c_entry.grid(column=1, row=3)
        ToolTip(c_entry, "Nhập số c")
        
    def calculate(self):
        try:
            a_val = float(self.a.get())  
            b_val = float(self.b.get())  
            c_val = float(self.c.get())  

            if a_val == 0:  
                if b_val == 0:
                    if c_val == 0:
                        self.result.set("Phương trình có vô số nghiệm")
                    else:
                        self.result.set("Phương trình vô nghiệm")
                else:
                    x = -c_val / b_val
                    self.result.set(f"Nghiệm x = {x:.2f}")
            else:
                delta = b_val**2 - 4 * a_val * c_val
                if delta > 0:
                    x1 = (-b_val + math.sqrt(delta)) / (2 * a_val)
                    x2 = (-b_val - math.sqrt(delta)) / (2 * a_val)
                    self.result.set(f"Nghiệm x1 = {x1:.2f}, x2 = {x2:.2f}")
                elif delta == 0:
                    x = -b_val / (2 * a_val)
                    self.result.set(f"Nghiệm kép x = {x:.2f}")
                else:
                    self.result.set("Phương trình vô nghiệm (không có nghiệm thực)")
        except ValueError:
            messagebox.showerror("Error", "Tham số không hợp lệ")
