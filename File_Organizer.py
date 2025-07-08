import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File type folders
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Others": []
}

def organize_files():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(file.endswith(ext) for ext in extensions):
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file))
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))

    messagebox.showinfo("Done", "Files have been organized!")

# GUI setup
root = tk.Tk()
root.title("File Organizer")
root.geometry("300x150")

tk.Label(root, text="Click the button to organize files").pack(pady=10)
tk.Button(root, text="Select Folder & Organize", command=organize_files).pack(pady=20)

root.mainloop()