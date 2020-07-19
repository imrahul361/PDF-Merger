from PyPDF2 import PdfFileMerger
import os

path = input("Enter the Path: ")
first_file = input("Enter the name of First File: ")+".pdf"
second_file = input("Enter the name of Second File: ")+".pdf"
pdf_files = [first_file, second_file]
merger = PdfFileMerger()
for files in pdf_files:
    merger.append(path+files)
merged_file = input("Enter the name of Merged File: ")
if not os.path.exists(path+merged_file+".pdf"):
    merger.write(path+merged_file+".pdf")
else:
    print("Try another Name as Name already exist")


