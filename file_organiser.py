#! "C:\\Users\\ksurowka\\PycharmProjects\\FileRenamer\\venv\\Scripts\\pythonw.exe"
# Modify the path above to lead to the desired pythonw.exe interpreter executable.
# This will prevent the script from opening a Python console window.
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

cwd = os.getcwd()
files = []
file_list = os.listdir()

root = tk.Tk()
root.overrideredirect(1)
root.withdraw()
dialog = messagebox.askokcancel(title="Warning",
                                message=f"This operation will rename {len(file_list)} files.\n"
                                        f"This cannot be undone. Proceed?")
root.destroy()

if dialog:
    padding = len(str(len(file_list)))

    for file in os.listdir():
        files.append((datetime.fromtimestamp(os.path.getmtime(file)),
                      file,
                      file.split('.')[-1]))

    for idx, file_entry in enumerate(files, start=1):
        _, filename, extension = file_entry
        os.rename(filename, f"{cwd}\\{idx:0>{padding}}.{extension}")
