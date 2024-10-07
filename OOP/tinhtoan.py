import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
from tong import Tong
from hieu import Hieu
from tich import Tich
from thuong import Thuong
from ptb1 import PTb1
from ptb2 import PTb2
class Calculator:
    def __init__(self, win):
        self.win = win
        self.win.title("Máy tính")

        self.tabControl = ttk.Notebook(self.win)
        self.tab1 = Tong(self.tabControl)
        self.tabControl.add(self.tab1, text="Tổng")
        self.tabControl.pack(expand=1, fill="both")  

        self.tab2 = Hieu(self.tabControl)
        self.tabControl.add(self.tab2, text="Hiệu")
        self.tabControl.pack(expand=1, fill="both")

        self.tab3 = Tich(self.tabControl)
        self.tabControl.add(self.tab3, text="Tích")
        self.tabControl.pack(expand=1, fill="both")

        self.tab4 = Thuong(self.tabControl)
        self.tabControl.add(self.tab4, text="Thương")
        self.tabControl.pack(expand=1, fill="both")

        self.tab5 = PTb1(self.tabControl)
        self.tabControl.add(self.tab5, text="Phương trình bậc 1")
        self.tabControl.pack(expand=1, fill="both")

        self.tab6 = PTb2(self.tabControl)
        self.tabControl.add(self.tab6, text="Phương trình bậc 2")
        self.tabControl.pack(expand=1, fill="both")
        self.create_menu()

    def create_menu(self):
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command= win.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)  
        menu_bar.add_cascade(label="Help", menu=help_menu)  
        help_menu.add_command(label="About", command=self._msgBox)
        
        self.win.config(menu=menu_bar)
    def _msgBox(self):
        msg.showinfo('Calculator Message Info Box', 'Đây là máy tính đơn giản sử dụng tkinter\n Truong Viet Vu_2274802011045')

    
if __name__ == "__main__":
    win = tk.Tk()
    app = Calculator(win)

    win.mainloop()
    