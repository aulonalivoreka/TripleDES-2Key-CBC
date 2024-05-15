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

