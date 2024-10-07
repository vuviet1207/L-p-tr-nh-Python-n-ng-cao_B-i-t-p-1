from phuongthuc import TinhToan
from tkinter import messagebox
class Tong(TinhToan):
    def __init__(self, parent):
        super().__init__(parent, "Tính Tổng")

    def calculate(self):
        try:
            a_val = float(self.a.get())  
            b_val = float(self.b.get())  
            x=a_val+b_val
         
            self.result.set(f"{self.a.get()}+{self.b.get()} = {x:.2f}")
        except ValueError:
                messagebox.showerror("Error", "Tham số không hợp lệ")