import os
import sys
import winreg

cwd = os.getcwd()

python_exe = sys.executable.replace("python", "pythonw")

key_path = r"Directory\\Background\\shell\\Organiser"

key = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, key_path)

winreg.SetValue(key, '', winreg.REG_SZ, "&Organise folder")

key1 = winreg.CreateKeyEx(key, r"command")
winreg.SetValue(key1, '', winreg.REG_SZ, python_exe + f' "{cwd}\\file_organiser.pyw"')
