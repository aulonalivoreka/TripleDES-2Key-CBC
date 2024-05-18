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

def add_label(self, parent, text, side=tk.TOP):
        # Method to add a label to a parent frame
        label = tk.Label(parent, text=text, font=("Georgia", 12), background='#f7f7f7')
        label.pack(side=side, padx=5, pady=5)
        return label

def add_entry(self, parent, side=tk.TOP):
        # Method to add an entry field to a parent frame
        entry = tk.Entry(parent, show="*", font=("Georgia", 12), background='white', borderwidth=2, relief='groove')
        entry.pack(side=side, padx=5, pady=5)
        return entry

def add_button(self, parent, text, command, bg, active_bg, side=tk.TOP):
        # Method to add a button to a parent frame
        button = tk.Button(parent, text=text, font=("Georgia", 12), background=bg, foreground='white',
                           activebackground=active_bg, activeforeground="white",
                           borderwidth=0, relief='solid', command=command)
        button.pack(side=side, padx=5, pady=5)
        return button

def add_radiobutton(self, parent, text, value, side=tk.TOP):
        # Method to add a radio button to a parent frame
        radio = tk.Radiobutton(parent, text=text, variable=self.action_choice, value=value,
                               font=("Georgia", 12), background='#f7f7f7', activebackground='#f7f7f7')
        radio.pack(side=side, padx=5, pady=5)
        return radio
    
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

     if not self.selected_file:
            messagebox.showerror("Error", "Please choose a file.")
            return

        try:
            with open(self.selected_file, "rb") as file:
                file_data = file.read()

    except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
            return
        
     action = self.action_choice.get()  # Get selected action
     if action == "encrypt":
            output_data = self.perform_encryption(file_data, formatted_key1, formatted_key2)
            output_filename = os.path.splitext(self.selected_file)[0] + "_encrypted" + os.path.splitext(self.selected_file)[1]
    else:
        output_data = self.perform_decryption(file_data, formatted_key1, formatted_key2)
        if not output_data:
            return

            output_extension = os.path.splitext(self.selected_file)[1]
            output_filename = os.path.splitext(self.selected_file)[0] + "_decrypted" + output_extension

            with open(output_filename, "wb") as file:
            file.write(output_data)

        messagebox.showinfo("Complete", f"Operation complete. Output file: {output_filename}")


    # Format key, Encryption and Decryption Logic
    def format_key(self, key_input):
        # Method to format the key to ensure it is 8 bytes
        key = key_input.encode('utf-8')
        if len(key) > 8:
            messagebox.showerror("Error", "Key is too long.")
            return None
        if len(key) < 8:
            key = pad(key, DES.block_size, style='pkcs7')
        return key

    def perform_encryption(self, data, key1, key2):
        iv = os.urandom(DES.block_size)  # Generate a random IV
        padded_data = pad(data, DES.block_size)

        # Perform Triple DES encryption: E-D-E
        first_pass = self.encrypt_des(padded_data, key1, iv)
        second_pass = self.decrypt_des(first_pass, key2, iv)
        final_pass = self.encrypt_des(second_pass, key1, iv)

        return binascii.hexlify(iv + final_pass)  # Return hex-encoded result

def perform_decryption(self, data, key1, key2):
        try:
            # Extract IV and ciphertext from data
            iv = binascii.unhexlify(data[:DES.block_size * 2])
            ciphertext = binascii.unhexlify(data[DES.block_size * 2:])
        except binascii.Error:
            messagebox.showerror("Error", "Invalid encrypted data format.")
            return None

        # Perform Triple DES decryption: D-E-D
        first_pass = self.decrypt_des(ciphertext, key1, iv)
        second_pass = self.encrypt_des(first_pass, key2, iv)
        final_pass = self.decrypt_des(second_pass, key1, iv)

        try:
            return unpad(final_pass, DES.block_size)  # Remove padding and return
        except ValueError:
            messagebox.showerror("Error", "Decryption failed. Incorrect key combination.")
            return None
        
    def encrypt_des(self, data, key, iv):
        # Method to perform DES encryption
        cipher = DES.new(key, DES.MODE_CBC, iv=iv)
        return cipher.encrypt(data)

    def decrypt_des(self, data, key, iv):
        # Method to perform DES decryption
        cipher = DES.new(key, DES.MODE_CBC, iv=iv)
        return cipher.decrypt(data)

    if __name__ == "__main__":
    main_root = tk.Tk()
    app = TripleDESApp(main_root)
    main_root.mainloop()

