import os
import shutil

folder = input("Enter the name of the folder: ")

if not os.path.exists(folder):
    os.makedirs(folder)     

for filename in os.listdir():
    if filename.startswith("Duplichecker"):
        shutil.move(filename, os.path.join(folder, filename))
        