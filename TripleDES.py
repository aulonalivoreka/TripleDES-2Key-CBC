import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os
import binascii


class TripleDESApp:
    def __init__(self, root_window):
        self.root_window = root_window
        self.initialize_gui()

    def initialize_gui(self):
        self.root_window.title("Triple DES Encrypt/Decrypt")
        self.root_window.geometry("800x250")
        self.center_window_on_screen()  # Center the window on the screen

        self.root_window.configure(background='#f7f7f7')  # Set background color

        self.add_widgets()  # Add GUI widgets

    def center_window_on_screen(self):
        # Calculate position to center window
        screen_w = self.root_window.winfo_screenwidth()
        screen_h = self.root_window.winfo_screenheight()
        position_x = (screen_w - 800) // 2
        position_y = (screen_h - 250) // 2
        self.root_window.geometry(f"800x250+{position_x}+{position_y}")

        def add_widgets(self):

            # Frame for Key 1 input
            key1_frame = tk.Frame(self.root_window, background='#f7f7f7')
            key1_frame.pack(pady=5)

            self.add_label(key1_frame, "Enter Key 1 (Up to 8 chars):", side=tk.LEFT)
            self.key1_input = self.add_entry(key1_frame, side=tk.LEFT)

            # Frame for Key 2 input
            key2_frame = tk.Frame(self.root_window, background='#f7f7f7')
            key2_frame.pack(pady=5)

            self.add_label(key2_frame, "Enter Key 2 (Up to 8 chars):", side=tk.LEFT)
            self.key2_input = self.add_entry(key2_frame, side=tk.LEFT)

            # Frame for File Selection
            file_frame = tk.Frame(self.root_window, background='#f7f7f7')
            file_frame.pack(pady=5)

            self.filepath_label = self.add_label(file_frame, "Choose a file:", side=tk.LEFT)
            self.add_button(file_frame, "Select File", self.choose_file, bg='#0044cc', active_bg='#0033aa', side=tk.LEFT)

            # Frame for Action Buttons
            action_frame = tk.Frame(self.root_window, background='#f7f7f7')
            action_frame.pack(pady=10)

            self.add_label(action_frame, "Action:", side=tk.LEFT)
            self.action_choice = tk.StringVar(value="encrypt")  # Default action is encrypt
            self.add_radiobutton(action_frame, "Encrypt", "encrypt", side=tk.LEFT)
            self.add_radiobutton(action_frame, "Decrypt", "decrypt", side=tk.LEFT)

            # Frame for Execute Button
            execute_frame = tk.Frame(self.root_window, background='#f7f7f7')
            execute_frame.pack(pady=10)

            self.add_button(execute_frame, "Execute", self.execute_process, bg='#28a745', active_bg='#218838', side=tk.LEFT)


    
    def choose_file(self):
        self.selected_file = filedialog.askopenfilename(initialdir="/", title="Choose a File", filetypes=(("All files", "*.*"),))

    if self.selected_file:
            self.filepath_label.config(text=self.selected_file, font=("Georgia", 10, 'italic'))
    else:
            self.filepath_label.config(text="Choose a file:", font=("Georgia", 12))

    def execute_process(self):
        key1 = self.key1_input.get()
        key2 = self.key2_input.get()

     if not key1:
            messagebox.showerror("Error", "Key 1 must be provided and be no more than 8 characters.")
            return

     if not key2:
            messagebox.showerror("Error", "Key 2 must be provided and be no more than 8 characters.")
            return
         
        formatted_key1 = self.format_key(key1)
        formatted_key2 = self.format_key(key2)

    def format_key(self, key_input):
    # Method to format the key to ensure it is 8 bytes
    key = key_input.encode('utf-8')
    # Check if key length is greater than 8 bytes and truncate if necessary
    if len(key) > 8:
        messagebox.showinfo("Info", "Key is too long. It will be truncated to 8 characters.")
        key = key[:8]  # Truncate to 8 bytes
    # If key length is less than 8 bytes, pad it to reach 8 bytes
    elif len(key) < 8:
        messagebox.showinfo("Info", "Key is too short. It will be padded to 8 characters.")
        key = pad(key, DES.block_size, style='pkcs7')
    return key

    def perform_encryption(self, data, key1, key2):
    iv = b'fixedIV12345678'[:DES.block_size]
    encrypted_once = self.encrypt_des(data, key1, iv)
    static_iv = b'staticIV1234567'[:DES.block_size]
    decrypted_once = self.decrypt_des(encrypted_once, key2, static_iv)
    final_encryption = self.encrypt_des(decrypted_once, key1, iv)
   
    return binascii.hexlify(final_encryption)

    def perform_decryption(self, data, key1, key2):
    try:
        iv = binascii.unhexlify(data[:DES.block_size * 2])
        ciphertext = binascii.unhexlify(data[DES.block_size * 2:])
    except binascii.Error:
        messagebox.showerror("Error", "Invalid encrypted data format.")
        return None

    first_pass = self.decrypt_des(ciphertext, key1, iv)
    static_iv = b'staticIV1234567'[:DES.block_size]  # Using a different IV for middle step
    second_pass = self.encrypt_des(first_pass, key2, static_iv)
    final_pass = self.decrypt_des(second_pass, key1, iv)

    try:
        return unpad(final_pass, DES.block_size)
    except ValueError:
        messagebox.showerror("Error", "Decryption failed. Incorrect key combination.")
        return None
        
    def encrypt_des(self, data, key, iv):
    modified_iv = iv[::-1]
    cipher = DES.new(key, DES.MODE_CBC, iv=modified_iv)
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

    def decrypt_des(self, data, key, iv):
    modified_iv = iv[::-1]
    cipher = DES.new(key, DES.MODE_CBC, iv=modified_iv)
    decrypted_data = cipher.decrypt(data)
    return decrypted_data

    if __name__ == "__main__":
    main_root = tk.Tk()
    app = TripleDESApp(main_root)
    main_root.mainloop()

