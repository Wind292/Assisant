
import tkinter as tk    
from tkinter import filedialog
import subprocess
import os
import ctypes, sys


def install():
    global install_dir  # Access the global variable
    if install_dir == "": install_dir = "C:/Program Files/assistant"
    os.makedirs(install_dir + "/assistant")




def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Declare install_dir as a global variable
    install_dir = ""

    def open_settings_window():
        settings_window = tk.Toplevel(root)
        settings_window.title("Settings")
        settings_window.geometry("400x100")
        settings_window.resizable(False, False)
        
        # Function to choose directory
        def choose_directory():
            global install_dir  # Use global to modify the global variable
            directory_path = filedialog.askdirectory()
            if directory_path:
                directory_entry.delete(0, tk.END)
                directory_entry.insert(0, directory_path)
                install_dir = directory_path  # Update the global variable
        
        # Label, entry, and button for directory selection
        directory_frame = tk.Frame(settings_window)
        directory_frame.pack(pady=10)
        
        directory_label = tk.Label(directory_frame, text="Install Directory:")
        directory_label.pack(side="left")
        
        # Set initial directory path here
        initial_directory = "C:/Program Files/assistant"
        directory_entry = tk.Entry(directory_frame, width=30)
        directory_entry.insert(0, initial_directory)  # Insert the initial directory path
        directory_entry.pack(side="left")
        
        # Button to select directory
        select_dir_button = tk.Button(directory_frame, text="Select Dir", command=choose_directory, relief=tk.FLAT, fg="blue", cursor="hand2")
        select_dir_button.pack(side="left")

    # Main window
    root = tk.Tk()

    root.title("Assistant Setup")

    root.geometry("500x400")  # width x height
    root.resizable(False, False)

    text_label = tk.Label(root, text="Click to install Assistant",  font=("Arial", 30))
    text_label.pack(pady=10)
    
    install_button = tk.Button(root, text="Install", width=10, height=3, font=("Arial", 30), command=install)
    install_button.pack(pady=10)

    settings_button = tk.Button(root, text="Settings", command=open_settings_window, width=10, height=3, font=("Arial", 30))
    settings_button.pack(pady=10)

    root.mainloop()


else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0x400)




