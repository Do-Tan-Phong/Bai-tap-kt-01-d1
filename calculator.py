import tkinter as tk
from tkinter import messagebox

def tinh_toan(phep_tinh):
    try:
        so1 = float(entry_so1.get())
        so2 = float(entry_so2.get())
        
        if phep_tinh == '+':
            ket_qua = so1 + so2
        elif phep_tinh == '-':
            ket_qua = so1 - so2
        elif phep_tinh == '*':
            ket_qua = so1 * so2
        elif phep_tinh == '/':
            if so2 == 0:
                messagebox.showerror("Lỗi", "Không thể chia cho 0!")
                return
            ket_qua = so1 / so2
            
        label_ket_qua.config(text=f"Kết quả: {ket_qua}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Máy tính đơn giản")
window.geometry("400x300")
window.configure(bg='#f0f0f0')
# Đặt cửa sổ ở giữa màn hình
window.eval('tk::PlaceWindow . center')

# Tạo các widget với style đẹp hơn
tk.Label(window, text="Số thứ nhất:", font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
entry_so1 = tk.Entry(window, font=('Arial', 12), width=20)
entry_so1.pack()

tk.Label(window, text="Số thứ hai:", font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
entry_so2 = tk.Entry(window, font=('Arial', 12), width=20)
entry_so2.pack()

# Frame chứa các nút phép tính
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

# Tạo các nút phép tính với style đẹp hơn
button_style = {'font': ('Arial', 14), 'width': 3, 'height': 1, 'bg': '#4CAF50', 'fg': 'white'}

tk.Button(frame_buttons, text="+", command=lambda: tinh_toan('+'), **button_style).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="-", command=lambda: tinh_toan('-'), **button_style).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="×", command=lambda: tinh_toan('*'), **button_style).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="÷", command=lambda: tinh_toan('/'), **button_style).pack(side=tk.LEFT, padx=5)

# Label hiển thị kết quả với style đẹp hơn
label_ket_qua = tk.Label(window, text="Kết quả: ", font=('Arial', 14, 'bold'), bg='#f0f0f0')
label_ket_qua.pack(pady=20)

# Thêm nút Xóa để làm mới các ô nhập liệu
def xoa_du_lieu():
    entry_so1.delete(0, tk.END)
    entry_so2.delete(0, tk.END)
    label_ket_qua.config(text="Kết quả: ")

tk.Button(window, text="Xóa", command=xoa_du_lieu, font=('Arial', 12), bg='#ff9800', fg='white').pack(pady=10)

# Chạy ứng dụng
window.mainloop()