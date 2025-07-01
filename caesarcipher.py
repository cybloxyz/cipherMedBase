import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A')  if char.isupper()  else ord('a')
            result += chr((ord(char)- base + shift )% 26 + base)
        else:
            result += char
           
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def handle_encrypt():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        result = encrypt(text, shift)
        result_label.config(text=f"hasil enkripsi kamu : {result}")
    except ValueError:
        messagebox.showerror("hehe gimana sih..", "shift nya BELUM DIMASUKIN!!")

def handle_decrypt():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        result = decrypt(text, shift)
        result_label.config(text=f"hasil dekripsi kamu : {result}")
        
    except ValueError:
        messagebox.showerror("hehe gimana sih..", "shift nya BELUM DIMASUKIN!!")

 
root = tk.Tk()
root.title("PESAN RAHASIA")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="yang mau di rahasia-in : ").pack()
entry_text = tk.Entry(root, width=50)
entry_text.pack()

tk.Label(root, text="mau di geser berapa : ").pack()
entry_shift = tk.Entry(root, width=10)
entry_shift.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_encrypt = tk.Button(frame_buttons, text="enkripsi aja : ", command=handle_encrypt)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(frame_buttons, text="terjemahin enkrip : ", command=handle_decrypt)
btn_decrypt.grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="hasilnya disini", wraplength=380)
result_label.pack(pady=10)

root.mainloop()

root = tk.Tk()
root.title("🔒 PESAN RAHASIA")
root.geometry("450x300")
root.resizable(False, False)
root.configure(bg="#f0f4ff")

font_title = ("Helvetica", 14, "bold")
font_label = ("Helvetica", 11)
font_entry = ("Helvetica", 10)

tk.Label(root, text="Masukkan pesan rahasia:", font=font_label, bg="#f0f4ff").pack(pady=(10, 5))
entry_text = tk.Entry(root, width=50, font=font_entry)
entry_text.pack(pady=(0, 10))

tk.Label(root, text="Geser huruf sebanyak (angka):", font=font_label, bg="#f0f4ff").pack(pady=(5, 5))
entry_shift = tk.Entry(root, width=10, font=font_entry, justify='center')
entry_shift.pack(pady=(0, 10))

frame_buttons = tk.Frame(root, bg="#f0f4ff")
frame_buttons.pack(pady=10)

btn_encrypt = tk.Button(frame_buttons, text="🔐 Enkripsi", font=font_label, bg="#c2e7ff", fg="black", command=handle_encrypt)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(frame_buttons, text="🔓 Dekripsi", font=font_label, bg="#ffd6d6", fg="black", command=handle_decrypt)
btn_decrypt.grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="Hasil akan muncul di sini", wraplength=380, font=("Courier New", 11), bg="#f0f4ff", fg="darkblue", justify="center")
result_label.pack(pady=15)

root.mainloop()

