import tkinter as tk
from tkinter import messagebox

# Encryption
def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

# Decryption
def decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

# 🔐 Brute Force Attack
def brute_force(ciphertext):
    results = ""
    
    for shift in range(26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decrypted += chr((ord(char) - base - shift) % 26 + base)
            else:
                decrypted += char
        
        results += f"Shift {shift}: {decrypted}\n"
    
    return results

# GUI Functions
def encrypt_text():
    message = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        encrypted = encrypt(message, shift)
        
        encrypted_text.delete("1.0", tk.END)
        encrypted_text.insert(tk.END, encrypted)
        
        # Auto decrypt
        decrypted_text.delete("1.0", tk.END)
        decrypted_text.insert(tk.END, decrypt(encrypted, shift))
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")

# 🔐 Brute Force Button Function
def brute_force_text():
    ciphertext = input_text.get("1.0", tk.END).strip()
    
    if not ciphertext:
        messagebox.showerror("Error", "Enter ciphertext first")
        return
    
    result = brute_force(ciphertext)
    
    encrypted_text.delete("1.0", tk.END)
    encrypted_text.insert(tk.END, result)

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Tool (Encryption + Attack Simulation)")
root.geometry("520x600")

# Input
tk.Label(root, text="Enter Message:", font=("Arial", 12)).pack()
input_text = tk.Text(root, height=3)
input_text.pack(pady=5)

tk.Label(root, text="Enter Shift:", font=("Arial", 12)).pack()
shift_entry = tk.Entry(root)
shift_entry.pack(pady=5)

# Buttons
tk.Button(root, text="Encrypt & Decrypt", command=encrypt_text, bg="lightblue").pack(pady=10)
tk.Button(root, text="Brute Force Attack", command=brute_force_text, bg="lightcoral").pack(pady=5)

# Encrypted output
tk.Label(root, text="Encrypted / Brute Force Output:", font=("Arial", 12)).pack()
encrypted_text = tk.Text(root, height=12)
encrypted_text.pack(pady=5)

# Decrypted output
tk.Label(root, text="Decrypted Text:", font=("Arial", 12)).pack()
decrypted_text = tk.Text(root, height=3)
decrypted_text.pack(pady=5)

root.mainloop()