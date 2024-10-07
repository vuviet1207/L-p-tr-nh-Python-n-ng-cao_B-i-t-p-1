from phuongthuc import TinhToan
from tkinter import messagebox
class PTb1(TinhToan):
    def __init__(self, parent):
        super().__init__(parent, "Giải phương trình bậc 1 ax + b = 0")

    def calculate(self):
        try:
            a_val = float(self.a.get())  
            b_val = float(self.b.get())  
            if a_val == 0:
                if b_val == 0:
                    self.result.set("Phương trình có vô số nghiệm")
                else:
                    self.result.set("Phương trình vô nghiệm")
            else:
                x = -(b_val) / a_val
                self.result.set(f"Nghiệm x = {x:.2f}")
         
            self.result.set(f"kết quả = {x:.2f}")
        except ValueError:
                messagebox.showerror("Error", "Tham số không hợp lệ")