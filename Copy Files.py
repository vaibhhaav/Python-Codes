import shutil

src_path = r"D:\B. Tech. VIT Bhopal\2nd Year (2024-2025)\3rd Semester (Fall Semester)\Python Programming\Python-codes\write_demo.txt"
dst_path = r"D:\B. Tech. VIT Bhopal\2nd Year (2024-2025)\3rd Semester (Fall Semester)\Python Programming\Python-codes\writes_demo.txt"
shutil.copy(src_path,dst_path)
print('Copied')