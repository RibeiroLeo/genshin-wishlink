import os

base = os.path.expandvars(r"%userprofile%\AppData\LocalLow\miHoYo")
for root, dirs, files in os.walk(base):
    for file in files:
        if file.endswith(".txt") or "log" in file.lower():
            print(os.path.join(root, file))
