import tkinter as tk
import random

# Hàm để tạo mật khẩu ngẫu nhiên
def generate_password():
    # Lấy tên người dùng từ ô nhập
    username = name_entry.get()
    
    if not username:
        password_label.config(text="Vui lòng nhập tên!")
        return
    
    # Các dãy ký tự trong bảng mã Unicode (A-Z, a-z)
    char_set = list(range(65, 91)) + list(range(97, 123))
    
    # Tạo mật khẩu dài 20 ký tự ngẫu nhiên
    password = ''.join(chr(random.choice(char_set)) for _ in range(20))
    
    # Cập nhật mật khẩu lên giao diện
    password_entry.delete(0, tk.END)  # Xóa mật khẩu cũ
    password_entry.insert(0, password)  # Hiển thị mật khẩu mới
    
    # Lưu mật khẩu vào file với ghi bản quyền
    with open(f'{username}_password.txt', 'w', encoding='utf-8') as file:
        file.write(f"# Bản quyền mật khẩu\n")
        file.write(f"# Được tạo tự động bằng chương trình Tạo Mật Khẩu Ngẫu Nhiên\n\n")
        file.write(f"Mật khẩu cho {username}: {password}\n")
        file.write(f"\n# Bạn có thể sao chép mật khẩu từ đây.")
    
    # Thông báo lưu thành công
    success_label.config(text=f"Mật khẩu đã được lưu vào file '{username}_password.txt'.")

# Tạo cửa sổ giao diện chính
root = tk.Tk()
root.title("Tạo Mật Khẩu Ngẫu Nhiên")
root.geometry("400x350")

# Thêm label cho tên người dùng
name_label = tk.Label(root, text="Nhập tên của bạn:", font=('Arial', 12))
name_label.pack(pady=10)

# Thêm ô nhập tên
name_entry = tk.Entry(root, font=('Arial', 12))
name_entry.pack(pady=5)

# Thêm nút tạo mật khẩu
generate_button = tk.Button(root, text="Tạo Mật Khẩu", command=generate_password, font=('Arial', 14))
generate_button.pack(pady=20)

# Thêm Entry để hiển thị mật khẩu và cho phép sao chép
password_label = tk.Label(root, text="Mật khẩu sẽ được hiển thị ở đây", font=('Arial', 14))
password_label.pack(pady=10)

password_entry = tk.Entry(root, font=('Arial', 14), width=30)
password_entry.pack(pady=10)

# Thêm nhãn để thông báo lưu thành công
success_label = tk.Label(root, text="", font=('Arial', 12, 'italic'), fg='green')
success_label.pack(pady=10)

# Chạy giao diện
root.mainloop()
