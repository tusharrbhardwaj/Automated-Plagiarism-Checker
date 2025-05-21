import os, os.path

#Following library is to move file from one directory to another, identified with the help of OS library
import shutil

folder = 'unit4'

print("Removing additional files")
dpath = '/Users/tushar/Documents/GitHub/file_splitter/pdffolder'
shutil.rmtree(dpath)
print("Deleted all downloaded files from pdf-folder")

os.remove(f'{folder}merged.pdf')
os.remove(f'{folder}prep.pdf')
os.remove(f'{folder}-plag-reportfile.txt')
dpath = f'/Users/tushar/Documents/GitHub/file_splitter/{folder}'
shutil.rmtree(dpath)

print("All additional files delted successfully")
