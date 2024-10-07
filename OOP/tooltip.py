import tkinter as tk
class ToolTip(object):
    def __init__(self, widget, tip_text=None): 
        self.widget = widget
        self.tip_text = tip_text
        self.tip_window = None  # Khởi tạo tip_window
        widget.bind('<Enter>', self.mouse_enter)
        widget.bind('<Leave>', self.mouse_leave)
    
    def mouse_enter(self, _event):  
        self.show_tooltip()
    
    def mouse_leave(self, _event):  
        self.hide_tooltip()

    def show_tooltip(self):  
        if self.tip_window:  # Kiểm tra xem tip_window có tồn tại không
            return  # Nếu đã có, không làm gì cả
            
        # Tính toán vị trí tooltip
        x_left = self.widget.winfo_rootx()  
        y_top = self.widget.winfo_rooty() - 18
        
        # Tạo cửa sổ tooltip
        self.tip_window = tk.Toplevel(self.widget) 
        self.tip_window.overrideredirect(True)  # Không có viền
        self.tip_window.geometry("+%d+%d" % (x_left, y_top))  
        
        # Tạo nhãn cho tooltip
        label = tk.Label(self.tip_window, text=self.tip_text, 
                         justify=tk.LEFT, background="#ffffe0", 
                         relief=tk.SOLID, borderwidth=1, 
                         font=("tahoma", "8", "normal"))  
        label.pack(ipadx=1)
            
    def hide_tooltip(self):  
        if self.tip_window:  # Kiểm tra xem tip_window có tồn tại không
            self.tip_window.destroy()  # Hủy bỏ cửa sổ tooltip
            self.tip_window = None